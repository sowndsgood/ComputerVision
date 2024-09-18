import cv2
import numpy as np
from matplotlib import pyplot as plt

s = 125
l = range(0, 255, 2)
h = 155

cols = 10
rows = int((len(l) / cols) + 1)

fig, axes = plt.subplots(rows, cols)
ncols = axes.shape[1]
print(axes.shape)
fig.suptitle("Varying L channel")
for i, lval in enumerate(l):
    color = (h, lval, s)
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    img[:] = color
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_HLS2RGB)
    r = int(i / ncols)
    c = i % ncols
    axes[r][c].imshow(img_rgb)
    axes[r][c].axis('off')
    
plt.show()