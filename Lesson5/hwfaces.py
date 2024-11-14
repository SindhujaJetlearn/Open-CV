#### Count the number of circles in the image 
## Refer - https://www.geeksforgeeks.org/find-circles-and-ellipses-in-an-image-using-opencv-python/#

import cv2
import numpy as np
image = cv2.imread('eyes.jpg',0)

# Give a basic overview of the SimpleBlobDetecter function, Why it is used and What are the parameters required.

# Set our filtering parameters Initialize parameter settiing using cv2.SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()

# Set Area filtering parameters
params.filterByArea = True
params.minArea = 100
# Set Circularity filtering parameters
params.filterByCircularity = True
params.minCircularity = 0.01
# Set Convexity filtering parameters
params.filterByConvexity = True
params.minConvexity = 0.5
# Set inertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.1
# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
	
# Detect blobs
keypoints = detector.detect(image)

# Draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#number_of_blobs = len(keypoints)
#text = "Number of eyes: " + str(len(keypoints))
#cv2.putText(blobs, text, (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

# Show blobs
cv2.imshow("Filtering Circular Blobs Only", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()


