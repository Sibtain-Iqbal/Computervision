import numpy as np
import cv2  


img = cv2.imread("hello.png")
res_img = cv2.resize(img,(300,700))
polygin  = cv2.polylines(img = img ,
 pts =[np.array([
    [100,200],
    [200,300],[400,300],[400,500],[150,300]
 ])]
  ,
  isClosed= True ,
  color = (0,155,0),
  thickness= 14,
  lineType = 16 
 
 )

cv2.imshow("Detection Line",polygin)
cv2.waitKey(0)
cv2.destroyAllWindows(0)