import cv2
import numpy as np


cap = cv2.VideoCapture(0)

# Capture a frame
ret, img = cap.read()
cap.release()  

if not ret:
    print("Failed to capture image")
    exit()

text = input("What Your Name :  ")


(h, w, _) = img.shape

font = cv2.FONT_HERSHEY_DUPLEX
font_scale = 1
thickness = 3


(text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)


x = (w - text_width) // 2
y = 50  

overlay = img.copy()
cv2.rectangle(overlay, (x - 10, y - text_height - 10), (x + text_width + 10, y + 10), (0, 0, 0), -1)
alpha = 0.5  # Transparency level
cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

# Add shadow effect (black text offset slightly)
cv2.putText(img, text, (x + 2, y + 2), font, font_scale, (0, 0, 0), thickness + 2, cv2.LINE_AA)

# Add main text
cv2.putText(img, text, (x, y), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

resized_img = cv2.resize(img, (400, 600))


cv2.imshow("Captured Image with Text", resized_img)

# Save the modified image
cv2.imwrite("output_with_text.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
