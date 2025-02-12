import cv2
import numpy as np
import os



img2= cv2.imread('IMG_0886.JPG')
img1 = cv2.imread('image.jpg.png')

res_img = cv2.resize(img2,(300,600))

h= np.hstack((res_img,res_img,res_img,res_img,res_img,res_img)) #the hstack will joi  two or multiples arrays in one dimesioonalyy


v  = np.vstack((h,h,h,h,h,h))

cv2.imshow("resize the image" , v)

cv2.waitKey(0)

cv2.destroyAllWindows(0)

