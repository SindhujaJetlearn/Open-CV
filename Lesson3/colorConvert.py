import cv2
image=cv2.imread("pika.png")

#HSV color model .. H- hue  S-saturation V-value
hsvImage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

cv2.imshow("HSV Image",hsvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

