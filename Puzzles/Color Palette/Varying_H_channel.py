import cv2
import numpy as np
from matplotlib import pyplot as plt

s = 125
l = 155
h = range(0, 255, 2)

cols = 10
rows = int((len(h) / cols) + 1)

fig, axes = plt.subplots(rows, cols)
ncols = axes.shape[1]
print(axes.shape)
fig.suptitle("Varying H channel")
for i, hval in enumerate(h):
    color = (hval, l, s)
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    img[:] = color
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_HLS2RGB)
    r = int(i / ncols)
    c = i % ncols
    axes[r][c].imshow(img_rgb)
    axes[r][c].axis('off')
    
plt.show()