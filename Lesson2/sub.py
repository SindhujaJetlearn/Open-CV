# Subtraction of images

import cv2 

image1 = cv2.imread('input1.png') 
image2 = cv2.imread('input2.png')
  
sub = cv2.subtract(image1, image2)
  
cv2.imshow('Subtracted Image', sub)
  
cv2.waitKey(0)
cv2.destroyAllWindows()