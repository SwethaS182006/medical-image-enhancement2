import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr, structural_similarity as ssim
import matplotlib.pyplot as plt

# Step 1: Load the grayscale medical image
image_path = "a grayscale medical .png"
original = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if original is None:
          FileNotFoundError("Image not found. Please ensure 'Grayscale image.png' is available in the working directory.")

# Step 2: Denoising
denoised = cv2.fastNlMeansDenoising(original, None, h=10, templateWindowSize=7, searchWindowSize=21)

# Step 3: Sharpening
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
enhanced = cv2.filter2D(denoised, -1, kernel)

# Step 4: Image Quality Metrics
psnr_value = psnr(original, enhanced)
ssim_value = ssim(original, enhanced, data_range=enhanced.max() - enhanced.min())

print("\nImage Quality Metrics:")
print(f"PSNR (Peak Signal-to-Noise Ratio): {psnr_value:.2f} dB")
print(f"SSIM (Structural Similarity Index): {ssim_value:.4f}\n")

# Step 5: Simulated Findings
findings = {
    "ventricles": "mild enlargement",
    "lesion": "no abnormal mass detected",
    "cortex": "normal thickness",
    "suggested_diagnosis": "early signs of hydrocephalus"
}

# Step 6: Generate Clinical Note
def generate_clinical_note(findings):
    note = (
        f"Clinical Imaging Report:\n"
        f"- Ventricular Status: {findings['ventricles']}\n"
        f"- Lesion Presence: {findings['lesion']}\n"
        f"- Cortical Thickness: {findings['cortex']}\n\n"
        f"Impression: {findings['suggested_diagnosis']}\n"
        f"Recommendation: Recommend follow-up with neurology and CSF flow study.\n"
    )
    return note

# Step 7: Map to ICD-10 Code
def map_to_icd10(diagnosis):
    icd_map = {
        "hydrocephalus": "G91.9",
        "brain tumor": "D43.2",
        "normal": "Z00.00"
    }
    for key in icd_map:
        if key in diagnosis.lower():
            return icd_map[key]
    return "R99"  # Unknown or unspecified diagnosis

# Step 8: Display Clinical Note and ICD-10 Code
note = generate_clinical_note(findings)
code = map_to_icd10(findings["suggested_diagnosis"])

print(note)
print(f"ICD-10 Code: {code}\n")

# Step 9: Display Images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
titles = ["Original Image", "Denoised Image", "Enhanced Image"]
images = [original, denoised, enhanced]

for ax, img, title in zip(axes, images, titles):
    ax.imshow(img, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()

# Step 10: Save Enhanced Image
cv2.imwrite("enhanced_output.png", enhanced)
print("Enhanced image saved as 'enhanced_output.png'")