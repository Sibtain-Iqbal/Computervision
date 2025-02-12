import cv2
import numpy


gray = cv2.imread("grayscale.png",cv2.IMREAD_GRAYSCALE)

color1 = cv2.applyColorMap(gray, cv2.COLORMAP_HOT) 
color2 = cv2.applyColorMap(gray, cv2.COLORMAP_COOL) 
color3 = cv2.applyColorMap(gray, cv2.COLORMAP_HSV) 
color4= cv2.applyColorMap(gray, cv2.COLORMAP_RAINBOW) 
color5 = cv2.applyColorMap(gray, cv2.COLORMAP_OCEAN) 



h = numpy.hstack((color1,color2,color3,color4,color5))
v = numpy.vstack((h))
resizes  = cv2.resize(v,(500,900))
cv2.imshow("Color map ",resizes)
cv2.waitKey(0)
cv2.destroyAllWindows(0)