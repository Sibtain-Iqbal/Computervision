import cv2

img = cv2.imread(r"D:\Computervision\detectionBox_Image\hello.png")

res_img = cv2.resize(img,(340,500))

h,w = res_img.shape[0],res_img.shape[1]

rotate_img = cv2.getRotationMatrix2D((w/2 , h/2),90,1)
l = cv2.warpAffine(res_img,rotate_img,(w,h))
cv2.imshow("scale and rotate images",l)
cv2.waitKey(0)
cv2.destroyAllWindows