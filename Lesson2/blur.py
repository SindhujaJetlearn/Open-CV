import cv2
image = cv2.imread("pika.png")
cv2.imshow('Original Image', image)

Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)

median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Gaussian Blur - used mostly in machine learning preprocessing steps
#Gaussian blur describes blurring an image by a Gaussian function. 
#It is a widely used effect in graphics software, typically to reduce image noise and reduce detail.
#(img, Kernal_size ,std_dev)

# Median Blur -widely used in digital image processing because, under certain conditions, 
# it preserves edges while removing noise.
#(img,Kernal_size)

# Bilateral Blur - only sharp edges are preserved here
#(img,diameter of each pixel neighborhood,sigmaColor,sigmaSpace)
