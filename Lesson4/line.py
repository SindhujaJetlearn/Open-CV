#Draw a line on the image
# importing cv2 
import cv2 
image = cv2.imread("pika.png")

# top left corner of image
start_point = (0, 0)
#bottom right corner of image
end_point = (300, 250)

color = (0, 255, 0)

thickness = 9
  
  
image = cv2.line(image, start_point, end_point, color, thickness)
  

cv2.imshow("Image", image) 
cv2.waitKey(0)
cv2.destroyAllWindows()



