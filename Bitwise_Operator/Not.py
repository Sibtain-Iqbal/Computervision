import cv2
import numpy as np

img2 = cv2.imread(r"D:\Computervision\Bitwise_Operator\984269812_3.png")
img1 = cv2.imread(r"D:\Computervision\Bitwise_Operator\images.png")


res = cv2.resize(img1,(500,500))
res2 = cv2.resize(img2,(500,500))

ands = cv2.bitwise_not(res,res2)

h = np.hstack((res,res2,ands))

cv2.imshow("Not oprtator perfom" , h)
cv2.waitKey(0)
cv2.destroyAllWindows(0)
