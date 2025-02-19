import cv2




image = cv2.imread(r"D:\Computervision\detectionBox_Image\hello.png")
print(image.shape)
cn = cv2.Canny(image,300,300)
print(cn.shape)

cv2.imshow("edge detection ",image)
cv2.imshow("wdge detection", cn)
cv2.waitKey(0)
cv2.destroyAllWindows(0)