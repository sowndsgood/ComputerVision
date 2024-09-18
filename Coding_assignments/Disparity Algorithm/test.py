import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load stereo images in grayscale
img1=cv.imread(r"D:\Journey\CV\Coding_assignments\Disparity Algorithm\data\artroom\im1.jpg",cv.IMREAD_GRAYSCALE)
img2=cv.imread(r"D:\Journey\CV\Coding_assignments\Disparity Algorithm\data\artroom\im2.jpg",cv.IMREAD_GRAYSCALE)

# Ensure images are the same size
if img1.shape != img2.shape:
    raise ValueError("Input images must have the same dimensions")

# Create StereoSGBM object with specific parameters
numDisparities = 16  # Must be a multiple of 16
blockSize = 5  # Odd number

sgbm = cv.StereoSGBM_create(
    minDisparity=0,
    numDisparities=numDisparities,
    blockSize=blockSize,
    P1=8 * 3 * blockSize**2,
    P2=32 * 3 * blockSize**2,
    disp12MaxDiff=1,
    uniquenessRatio=10,
    speckleWindowSize=100,
    speckleRange=32
)

# Compute the disparity map
disparity = sgbm.compute(img1, img2)

# Normalize the disparity map to the range [0, 255] for better visualization
disparity_normalized = cv.normalize(disparity, None, 0, 255, cv.NORM_MINMAX)
disparity_normalized = np.uint8(disparity_normalized)

# Save the normalized disparity map
cv.imwrite("disparity_sgbm.png", disparity_normalized)

# Display the disparity map with Matplotlib
plt.figure(figsize=(10, 8))
plt.imshow(disparity_normalized, cmap='jet')
plt.colorbar(label='Disparity Value')  # Add a colorbar to show the mapping
plt.title('Disparity Map with Jet Colormap (SGM)')
plt.show()
