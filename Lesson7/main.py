"""
Algorithm:
1. Capture and store the background frame [ This will be done for some seconds ]
2. Detect the red colored cloth using color detection and segmentation algorithm.
3. Segment out the red colored cloth by generating a mask. [ used in code ]
4. Generate the final augmented output to create a magical effect. [ video.mp4 ]
"""

import cv2
import numpy as np
import time

#to acess webcamera (0-inbuilt camera)
raw_video=cv2.VideoCapture(0)

# give the camera to warm up 
time.sleep(1)
count = 0
background = 0

#Capturing that background which would be used for masking later.
for i in range(60):
    return_val,background=raw_video.read()
    if return_val == False:
        continue

# flipping of the frame  
background = np.flip(background, axis = 1)

# we are reading from video - for output
while(raw_video.isOpened()):
    return_val, img = raw_video.read()
    if not return_val:
        break
    count = count+1
    img = np.flip(img, axis = 1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Mask1
    lower_red = np.array([100, 40, 40])
    upper_red = np.array([100, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    #Mask2
    lower_red = np.array([155, 40, 40])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1=mask1+mask2

    # For refining the image as image is raw and blurry after processing in HSV format
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8),iterations = 2)
    mask1 = cv2.dilate(mask1, np.ones((3,3), np.uint8), iterations = 1)

    mask2 = cv2.bitwise_not(mask1)

    #Masking process
    res1 = cv2.bitwise_and(background, background, mask = mask1)
    res2 = cv2.bitwise_and(img, img, mask = mask2)

    #0-brightness of the image
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    cv2.imshow("Invisible Man",final_output)

    k = cv2.waitKey(10)
    #27 - escape key
    if k == 27:
        break
