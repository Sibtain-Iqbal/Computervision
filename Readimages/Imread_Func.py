import cv2
import numpy as np


img0 = cv2.imread(r"D:\Computervision\Readimages\IMG_0886.JPG",cv2.IMREAD_COLOR) #load the olor image 
img1 = cv2.imread(r"D:\Computervision\Readimages\IMG_0886.JPG",cv2.IMREAD_GRAYSCALE)  #the image will show black
caps = cv2.imread(r"D:\Computervision\Readimages\IMG_0886.JPG",cv2.IMREAD_UNCHANGED)  #the image will show black
gray = cv2.imread("grayscale.png",cv2.IMREAD_GRAYSCALE)



h =np.hstack((img0,img0))

cap = cv2.resize(h,(500,700))
cv2.imshow("All Read Functions",cap)
cv2.waitKey(0)
cv2.destroyAllWindows(0)
