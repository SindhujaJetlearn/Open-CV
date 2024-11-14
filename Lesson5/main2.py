# Count the number of circles in the image 
#Refer - https://www.geeksforgeeks.org/find-circles-and-ellipses-in-an-image-using-opencv-python/#

import cv2
import numpy as np
image = cv2.imread('blobs.jpeg', 0)

# Give a basic overview of the SimpleBlobDetecter function, Why it is used and What are the parameters required.

# Set our filtering parameters Initialize parameter setting using SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()

# Set Area filtering parameters- This is to avoid any identification of any small dots present in the image that can be wrongly detected as a circle. 
params.filterByArea = True
params.minArea = 100

# Set Circularity filtering parameters - This helps us to identify, shapes that are more similar to a circle. 
params.filterByCircularity = True
params.minCircularity = 0.8

# Set Convexity filtering parameters -  Concavity in general, destroys the circularity. More is the convexity, the closer it is to a close circle. 
params.filterByConvexity = True
params.minConvexity = 0.9

# Set inertia filtering parameters - Oval shaped to perfect circle
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
	
# Detect blobs - number of circle
keypoints = detector.detect(image)
print(keypoints)
number_of_blobs = len(keypoints)
print("Number of blobs : ", number_of_blobs)


#drawKeypoints(input_image, key_points, output_image, colour, flag)
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(number_of_blobs)

#cv2.putText(image, text, position, font, fontScale, color, thickness)
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

# Show blobs
cv2.imshow("Result", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()