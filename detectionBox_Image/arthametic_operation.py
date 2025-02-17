import cv2

img1 = cv2.imread("hello.png")

img2 = cv2.imread(r"D:\Computervision\detectionBox_Image\istockphoto-505370599-1024x1024.jpg")

res1 = cv2.resize(img1,(400,700))
res2 = cv2.resize(img2,(400,700))

new_img = cv2.subtract(res1,res2)

cv2.imshow("bacgroundimage",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)