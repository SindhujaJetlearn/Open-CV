# import cv2

# img=cv2.imread("pika.png")
# cv2.imshow("Original Image",img)

# rotate_img1=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# cv2.ROTATE_180,cv2.ROTATE_90_COUNTERCLOCKWISE

# cv2.imshow('Rotated Image', rotate_img1)

# cv2.waitKey(0) 
# cv2.destroyAllWindows()


#Rotating an image
import cv2

img = cv2.imread("C:/Users/HP/Desktop/JL/OpenCV/Lesson3/pika.png")
(rows, cols) = img.shape[0:2]

# getRotationMatrix2D creates a matrix needed for transformation.
# We want matrix for rotation w.r.t center to 90 degree without scaling.

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)

#We use the function cv::warpAffine for that purpose. Applies a Rotation to the image after being transformed. 
#This rotation is with respect to the image center.
res = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Rotated Image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
#cv2.ROTATE_180,cv2.ROTATE_90_COUNTERCLOCKWISE





