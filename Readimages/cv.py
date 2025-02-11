import cv2


image1 = cv2.imread("image.jpg.png")  
image2 = cv2.imread("capture (1).png")  

  
cv2.imshow("Github Image", image1)
cv2.imshow("React Image", image2)

cv2.waitKey(100000)

cv2.destroyAllWindows()
