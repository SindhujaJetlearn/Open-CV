import cv2
image1 = cv2.imread("pika.png")
cv2.imshow("orignal", image1)
rotate_image = cv2.rotate(image1, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotated", rotate_image)
rotate_image1 = cv2.rotate(image1, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Rotated1", rotate_image1)
rotate_image2 = cv2.rotate(image1, cv2.ROTATE_180)
cv2.imshow("Rotated2", rotate_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()