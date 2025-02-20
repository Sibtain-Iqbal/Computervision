import cv2

cap = cv2.VideoCapture(0)

while True :
    r,frame = cap.read()
    if r == True :
        frame = cv2.resize(frame,(500,500))
        if cv2.waitKey(10) & 0xfff == ord("p"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows(0)
    