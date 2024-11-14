import cv2

img=cv2.imread("pika.png")
cv2.imshow("Original Image",img)

gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)

cv2.waitKey(0) 
cv2.destroyAllWindows()
