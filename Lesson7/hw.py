# Refer - https://www.geeksforgeeks.org/invisible-cloak-using-opencv-python-project/

import cv2
import numpy as np
import time

print(cv2.__version__)

raw_video = cv2.VideoCapture("video2.mp4")

time.sleep(1)
count = 0
background = 0


# The video has some seconds in the starting where the background is completely visible, Capturing that backgrund which would be used for masking later.
for i in range(60):
    return_val, background = raw_video.read()
    if return_val == False:
        continue
    
# mirror image .
background = np.flip(background, axis = 1)


while(raw_video.isOpened()):
    return_val, img = raw_video.read()
    if not return_val:
        break
    count += 1
    img = np.flip(img, axis = 1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #mask 1
    lower_green = np.array([25,50,50])
    upper_green = np.array([90,255,255])
    mask1 = cv2.inRange(hsv, lower_green, upper_green)
    
    #mask 2
    lower_green = np.array([25,50,50])
    upper_green = np.array([100,255,255])
    mask2 = cv2.inRange(hsv, lower_green, upper_green)

    # lower_green = np.array([40,100, 40])
    # upper_green = np.array([255, 100, 255])

    # mask1 = cv2.inRange(hsv, lower_green, upper_green)

    # lower_green = np.array([40, 155, 40])
    # upper_green = np.array([255, 180, 255])

    # mask2 = cv2.inRange(hsv, lower_green, upper_green)

    mask1 = mask1 + mask2

    # For refining the image as image is raw and blurry after processing in HSV format
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations = 2)
    mask1 = cv2.dilate(mask1, np.ones((3,3), np.uint8), iterations = 1)

    mask2 = cv2.bitwise_not(mask1)

    # The masking happens here. You are adding 2 images together
    res1 = cv2.bitwise_and(background, background, mask = mask1)
    res2 = cv2.bitwise_and(img, img, mask = mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("INVISIBLE MAN", final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break

