import cv2 as cv

# Load the image
image_path = r"D:\Journey\CV\Puzzles\Greenery\up.jpg"
image = cv.imread(image_path)

# Define the coordinates of the pixel (x, y)
x = 100  # Column index
y = 50   # Row index

# Access the pixel at (x, y)
(b, g, r) = image[y, x]

# Print the RGB values
print(f"RGB Values at ({x}, {y}): Red={r}, Green={g}, Blue={b}")

# Optional: Display the image and allow clicking to inspect pixel values
def mouse_callback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        b, g, r = image[y, x]
        print(f"RGB Values at ({x}, {y}): Red={r}, Green={g}, Blue={b}")

cv.imshow('Image', image)
cv.setMouseCallback('Image', mouse_callback)

cv.waitKey(0)
cv.destroyAllWindows()
