import cv2
import itertools
import numpy as np
from matplotlib import pyplot as plt
# Loading the left / right images

imgL = cv2.imread('D:\Journey\CV\Coding_assignments\Disparity Algorithm\data\curucle\im1.jpg', cv2.IMREAD_GRAYSCALE)
imgR = cv2.imread('D:\Journey\CV\Coding_assignments\Disparity Algorithm\data\curucle\im2.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(imgL)
plt.figure()
plt.imshow(imgR)
# Disparity estimation

stereo = cv2.StereoBM.create(numDisparities=32, blockSize=15)
disparity = stereo.compute(imgL,imgR)

cv2.imwrite('diparity-output.png', disparity)

plt.figure()
plt.imshow(disparity,cmap='jet')

nrows, ncols = disparity.shape
disparity = disparity.reshape(-1, nrows * ncols)
# filtering invalid disparities (-1)
# setting up row, col vectors

yx = list(itertools.product(range(nrows), range(ncols)))

x, y = list(zip(*yx))
x = np.array(x).reshape(-1, nrows*ncols)
y = np.array(y).reshape(-1, nrows*ncols)

mask = disparity > 0
disparity = disparity[mask] * 0.1

x = x[mask]
y = y[mask]
# Converting disparities to point cloud
# Converting disparities to point cloud

imgC = cv2.imread('D:\Journey\CV\Coding_assignments\Disparity Algorithm\data\curucle\im1.jpg', cv2.IMREAD_COLOR)
plt.imshow(imgC)

# Split the color channels
b, g, r = cv2.split(imgC)

# Flatten the channels to match the structure of other arrays
r = r.flatten()
g = g.flatten()
b = b.flatten()

# Apply the mask after splitting
r = r[mask.flatten()]
g = g[mask.flatten()]
b = b[mask.flatten()]

baseline = 0.1
focal_length = 150

zw = (baseline * focal_length) / disparity

cx = ncols / 2
cy = nrows / 2

xw = (x - cx) * zw / focal_length
yw = (y - cy) * zw / focal_length

data = np.stack([-xw, yw, zw, r, g, b], axis=0).T
np.savetxt('final.asc', data)