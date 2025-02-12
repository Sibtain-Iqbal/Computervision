import cv2
import numpy as np

# cap = cv2.VideoCapture('videoplayback(1).mp4')

cap = cv2.VideoCapture(0)

lower_color = np.array([0, 0, 0])  
upper_color = np.array([180, 50, 50]) 

while True:
    ret, frame = cap.read()
    if not ret:
        break  

    # Convert the frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_frame, lower_color, upper_color)


    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

   
    for contour in contours:
        if cv2.contourArea(contour) > 500: 
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 

    
    cv2.imshow('Object Tracking', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows(0)

