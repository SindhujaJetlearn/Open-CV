#### Draw a rectangle on the image
import cv2 
image = cv2.imread("pika.png")
  
#  top left corner
start_point = (5, 5)
#bottom right corner 
end_point = (220, 220) 

color = (255, 0, 0)

thickness = 2

image = cv2.rectangle(image, start_point, end_point, color, thickness)
  
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()



## Using thickness of -1 px to fill the rectangle by black color.
import cv2
image = cv2.imread("pika.png")

start_point = (50, 50)
end_point = (150, 150)
color = (0, 0, 0)
thickness = -1

image = cv2.rectangle(image, start_point, end_point, color, thickness)

cv2.imshow("output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()