import cv2
import numpy as np


image1 = cv2.imread("image.jpg.png")  
image2 = cv2.imread("capture (1).png")  

  
cv2.imshow("Github Image", image1)
cv2.imshow("React Image", image2)

cv2.waitKey(100000)

cv2.destroyAllWindows()

# resize the image

img1= cv2.imread('IMG_0886.JPG')
res_img = cv2.resize(img1,(100,200))
cv2.imshow("resize the image" , res_img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)


