import cv2


img = cv2.imread("hello.png")
res_img  = cv2.resize(img,(500,700))
box = cv2.rectangle(img =res_img , pt1 = (150,50),pt2=(350,350),color = (10,10,255),lineType=16,thickness = 3 )

cv2.imshow("detection box",box)
cv2.waitKey(0)
cv2.destroyAllWindows(0)