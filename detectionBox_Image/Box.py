import cv2


img = cv2.imread("hello.png")
box = cv2.rectangle(img = img , pt1 = (200,300),pt2=(100,300),color(0,0,255),lineType=16,
    thickness = 10 )

cv2.imshow("detection box",box)
cv2.waitKey(5000)
cv2.destroyAllWindows(5000)