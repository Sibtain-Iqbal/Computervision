import cv2
import numpy as np

img1 = cv2.imread(r"D:\Computervision\detectionBox_Image\istockphoto-505370599-1024x1024.jpg")
img2 = cv2.imread(r"D:\Computervision\detectionBox_Image\hello.png")


res = cv2.resize(img1,(500,500))
res2 = cv2.resize(img2,(500,500))

ands = cv2.bitwise_and(res,res2)

h = np.hstack((res,res2,ands))

cv2.imshow("And oprtator perfom" , h)
cv2.waitKey(0)
cv2.destroyAllWindows(0)
