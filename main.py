from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr, structural_similarity as ssim
import tempfile

app = FastAPI()

# Endpoint 1: Enhance image and return metrics
@app.post("/enhance_image")
async def enhance_image(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Load grayscale image
    original = cv2.imread(tmp_path, cv2.IMREAD_GRAYSCALE)
    if original is None:
        return JSONResponse(status_code=400, content={"error": "Invalid image file"})

    # Denoise
    denoised = cv2.fastNlMeansDenoising(original, None, h=10, templateWindowSize=7, searchWindowSize=21)

    # Sharpen
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    enhanced = cv2.filter2D(denoised, -1, kernel)

    # Metrics
    psnr_value = psnr(original, enhanced)
    ssim_value = ssim(original, enhanced, data_range=enhanced.max() - enhanced.min())

    # Save enhanced image
    output_path = tmp_path.replace(".png", "_enhanced.png")
    cv2.imwrite(output_path, enhanced)

    return {
        "psnr": round(psnr_value, 2),
        "ssim": round(ssim_value, 4),
        "enhanced_image_path": output_path
    }

# Endpoint 2: Generate clinical note from findings
@app.post("/generate_note")
async def generate_note_endpoint(findings: dict):
    note = (
        f"Clinical Imaging Report:\n"
        f"- Ventricular Status: {findings.get('ventricles', 'N/A')}\n"
        f"- Lesion Presence: {findings.get('lesion', 'N/A')}\n"
        f"- Cortical Thickness: {findings.get('cortex', 'N/A')}\n\n"
        f"Impression: {findings.get('suggested_diagnosis', 'N/A')}\n"
        f"Recommendation: Recommend follow-up with neurology and CSF flow study.\n"
    )
    return {"note": note}

# Endpoint 3: Map diagnosis to ICD-10 code
@app.post("/map_icd10")
async def map_icd10_endpoint(diagnosis: str):
    icd_map = {
        "hydrocephalus": "G91.9",
        "brain tumor": "D43.2",
        "normal": "Z00.00"
    }
    for key in icd_map:
        if key in diagnosis.lower():
            return {"icd_code": icd_map[key]}
    return {"icd_code": "R99"}  # Unknown or unspecified diagnosis