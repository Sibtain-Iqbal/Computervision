import cv2



image = cv2.imread(r"D:\Computervision\detectionBox_Image\hello.png")
if image is None :
    print("the image will be loading")

else:
    res_img = cv2.resize(image,(500,500))
    blurs = cv2.medianBlur(res_img, 3)    

    cv2.imshow("blur img ",blurs)
    cv2.waitKey(0)
    cv2.destroyAllWindows(0) 