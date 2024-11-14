# importing cv2 
import cv2 
image = cv2.imread("pika.png")

# Start coordinate, here (0, 0) represents the top left corner of image
start_point = (200, 0)
# End coordinate, here (250, 250) represents the bottom right corner of image
end_point = (0, 200)
# Green color in BGR
color = (0, 255, 0)
# Line thickness of 9 px
thickness = 9
  
# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
image = cv2.line(image, start_point, end_point, color, thickness)
# Start coordinate, here (0, 0) represents the top left corner of image
start_point = (200, 0)
# End coordinate, here (250, 250) represents the bottom right corner of image
end_point = (400, 200)

image2 = cv2.line(image, start_point, end_point, color, thickness)  


# Start coordinate, here (0, 0) represents the top left corner of image
start_point = (0, 200)
# End coordinate, here (250, 250) represents the bottom right corner of image
end_point = (400, 200)
image3 = cv2.line(image, start_point, end_point, color, thickness)  



# Start coordinate, here (5, 5) represents the top left corner of rectangle
start_point = (0, 200)
# Ending coordinate, here (220, 220) represents the bottom right corner of rectangle
end_point = (400, 400) 
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 5
  
# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image4 = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow("Image", image4) 
cv2.waitKey(0)
cv2.destroyAllWindows()