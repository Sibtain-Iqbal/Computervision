import cv2
import numpy 


img = cv2.imread("hello.png")
res_img = cv2.resize(img,(400,700))

lineimg = cv2.line(img = res_img,pt1 = (300,100),pt2 = (300,400),color = (0,255,0),thickness = 10,lineType = 4)

cv2.imshow("Detection box",lineimg)
cv2.waitKey(0)
cv2.destroyAllWindows(0)