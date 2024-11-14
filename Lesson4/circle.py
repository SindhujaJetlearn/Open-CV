#Draw the circle on the image

import cv2
image = cv2.imread("pika.png")

# Center coordinates
center_coordinates = (120, 50)
# Radius of circle
radius = 20
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 2

# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(image, center_coordinates, radius, color, thickness)

# Displaying the image
cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

 ## Using thickness of -1 px to fill the circle by chosen color. 

import cv2
image = cv2.imread("pika.png")

center_coordinates = (120, 100)
radius = 30
color = (0, 255, 0)
thickness = -1

image = cv2.circle(image, center_coordinates, radius, color, thickness)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()