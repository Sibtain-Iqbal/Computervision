import cv2



cap = cv2.VideoCapture(r"D:\Computervision\Slow_and_fast_video\detected_2025-02-17_12-48-30.mp4")
#take the input from use how much the video faster and slow
wt = int(input("Enter the wait time in ms: "))
while cap.isOpened():
    ret,frame = cap.read()
    frame = cv2.resize(frame,(500,500))
    if ret == True :
       
        cv2.imshow("slowmo",frame)
        if cv2.waitKey(wt) & 0xff == ord("q"):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()