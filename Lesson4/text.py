
	
# importing cv2
import cv2
image = cv2.imread("pika.png")

# orgin
pos = (150, 150)
# font
font = cv2.FONT_HERSHEY_SIMPLEX
# fontScale
fontScale = 1
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 2


image = cv2.putText(image, 'Hi Hello', pos, font, fontScale, color, thickness)

cv2.imshow("Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()