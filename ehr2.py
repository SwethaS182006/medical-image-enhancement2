import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr, structural_similarity as ssim
import matplotlib.pyplot as plt

# Step 1: Load the grayscale medical image
original = cv2.imread("Grayscale image.png", cv2.IMREAD_GRAYSCALE)

# Check if image loaded properly
if original is None:
    print(" Error: Image not found! Make sure 'input_medical_image.png' is in the same folder.")
    exit()

# Step 2: Apply denoising
denoised = cv2.fastNlMeansDenoising(original, None, h=10, templateWindowSize=7, searchWindowSize=21)

# Step 3: Apply sharpening filter
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
enhanced = cv2.filter2D(denoised, -1, kernel)

# Step 4: Calculate PSNR and SSIM
psnr_value = psnr(original, enhanced)
ssim_value = ssim(original, enhanced, data_range=enhanced.max() - enhanced.min())

# Step 5: Display PSNR and SSIM values
print("\n Image Quality Metrics:")
print(f" PSNR (Peak Signal-to-Noise Ratio): {psnr_value:.2f} dB")
print(f" SSIM (Structural Similarity Index): {ssim_value:.4f}\n")

# Step 6: Display original, denoised, and enhanced images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(original, cmap='gray')
axes[0].set_title("Original Image")
axes[0].axis('off')

axes[1].imshow(denoised, cmap='gray')
axes[1].set_title("Denoised Image")
axes[1].axis('off')

axes[2].imshow(enhanced, cmap='gray')
axes[2].set_title("Enhanced Image")
axes[2].axis('off')

plt.tight_layout()
plt.show()

# Step 7: Save the enhanced image
cv2.imwrite("enhanced_output.png", enhanced)
print(" Enhanced image saved as 'enhanced_output.png'")