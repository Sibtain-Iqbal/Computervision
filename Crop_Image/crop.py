import cv2


img = cv2.imread(r"D:\Computervision\Image_Text\Screenshot 2024-11-15 224644.png")
if img is None :
    print("Image couldnot found check image path again")
else:
    print("Image found")
print(img.shape)

crop =  img[300:400 , 300:400]
cv2.imshow("original image" , crop)

cv2.imshow("crop image" , img)

cv2.waitKey(0)
cv2.destroyAllWindows()