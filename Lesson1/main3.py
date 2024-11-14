import cv2
import os

img=cv2.imread('pika.png',0)
cv2.imshow("Pikachu in Black and White", img)

# change the path to where you wish to save the image
path="C:/Users/HP/Desktop/JL/OpenCV/Lesson1/"

#change directory 
os.chdir(path)

cv2.imwrite("blackandWhite.png",img)

print("Successfully Saved")

cv2.waitKey(delay = 5000)

cv2.destroyAllWindows()


