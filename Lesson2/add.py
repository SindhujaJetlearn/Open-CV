import cv2

image1=cv2.imread('input1.png')
image2=cv2.imread('input2.png')

# 0.5 and 0.4 are weights to be multiplied for each pixel, 
#0 is gamma_value (measurement of light)
addImage=cv2.addWeighted(image1,0.5,image2,0.4, 0)

cv2.imshow("Output",addImage)

cv2.waitKey(0) 
cv2.destroyAllWindows() 