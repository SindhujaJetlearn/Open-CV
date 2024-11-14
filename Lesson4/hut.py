import cv2
image = cv2.imread('pika.png')

start = (100,100)
end = (400, 300)
color=(0,0,0)
thickness=1
#base
cv2.rectangle(image, start,end,color,thickness)

color1 = (255, 0, 255)
thickness1 = 2
#top
cv2.line(image, (100,100),(250,0),color1,thickness1)
cv2.line(image, (400,100),(250,0),color1,thickness1)

cv2.imshow('Line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()