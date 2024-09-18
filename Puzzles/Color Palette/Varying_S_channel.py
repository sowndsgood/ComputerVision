import cv2
import numpy as np
from matplotlib import pyplot as plt

s = range(0, 255, 2)
l = 155
h = 155

cols = 10
rows = int((len(s) / cols) + 1)

fig, axes = plt.subplots(rows, cols)
ncols = axes.shape[1]
print(axes.shape)
fig.suptitle("Varying S channel")
for i, sval in enumerate(s):
    color = (h, l, sval)
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    img[:] = color
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_HLS2RGB)
    r = int(i / ncols)
    c = i % ncols
    axes[r][c].imshow(img_rgb)
    axes[r][c].axis('off')
    
plt.show()