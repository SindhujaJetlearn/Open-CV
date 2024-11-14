import cv2
import numpy as np

img=cv2.imread("pika.png")
cv2.imshow("Original",img)

#filter 3*3, 5*5 - Kernal
#kernel/filter is used for erosion as an input
#uint8 - unsigned integer of 8 bit

kernel=np.ones((5,5), np.uint8)
print(kernel)

erosion=cv2.erode(img,kernel)

cv2.imshow("Eroded Image", erosion) 
cv2.waitKey(0)
cv2.destroyAllWindows()