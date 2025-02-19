import cv2
import numpy as np
img = cv2.imread(r"D:\Computervision\detectionBox_Image\hello.png")

res_img = cv2.resize(img,(340,500))

h,w = res_img.shape[0],res_img.shape[1]

rotate_img = cv2.getRotationMatrix2D((w/2 , h/2),60,1)
l = cv2.warpAffine(res_img,rotate_img,(w,h))
merge = np.hstack((res_img,l))
cv2.imshow(" rotate images",merge)
# cv2.imshow("orignal image",res_img)
cv2.waitKey(0)
cv2.destroyAllWindows