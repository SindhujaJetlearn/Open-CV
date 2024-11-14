import cv2

#Read in greyScale
img = cv2.imread("C:/Users/HP/Desktop/JL/OpenCV/Lesson1/pika.png", 0)

cv2.imshow("Pikachu in Grayscale", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
