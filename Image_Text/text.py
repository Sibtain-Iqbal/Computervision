import cv2

imgs = cv2.imread("Screenshot 2024-11-15 224644.png")

texts = "Cute Dog"
img = imgs
org = (50,50) #50 pixels top 50 pixels vertical
fontFace = cv2.FONT_HERSHEY_DUPLEX
fontScale = 1
color = (0,0,0,255)
thickness = 3
lineType = cv2.LINE_8

cv2.putText(img,texts,org,fontFace,fontScale,color,thickness,lineType)
resize_img = cv2.resize(imgs,(300,500))
cv2.imshow("text in a image ", resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)