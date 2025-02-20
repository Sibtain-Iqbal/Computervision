import cv2
import numpy as np

# Load the image
image = cv2.imread(r"D:\Computervision\Image_Text\Screenshot 2024-11-15 224644.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Convert to binary using thresholding
_, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours and count objects
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
object_count = len(contours)

# Display result
cv2.putText(image, f"Objects Count: {object_count}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow("Objects Detected", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
