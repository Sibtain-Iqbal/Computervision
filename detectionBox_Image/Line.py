import cv2
import numpy 


img = cv2.imread("hello.png")
res_img = cv2.resize(img,(300,700))

lineimg = cv2.line(img = res_img,pt1 = (150,200),pt2 = (400,190),color = (0,255,0),thickness = 5,lineType = 4)

cv2.imshow("Detection Line",lineimg)
cv2.waitKey(0)
cv2.destroyAllWindows(0)