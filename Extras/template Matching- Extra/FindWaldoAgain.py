import cv2
import numpy as np

#should we load in grayscale?
img = cv2.imread("puzzle.jpg")
img2 = img.copy()

template = cv2.imread("WaldoLady.png")

h,w,c = template.shape

# All the 6 methods for comparison in a list
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

#using a sliding window method
#imagine the img is of size 4 by 4 (W,H)
#and the template is 2 by 2 (H,h), or the sliding window
#the total number of times, the sliding window will slide right will be
#W-w +1
# so imagine that the img is like this
#[]
#the sliding window will do this for each of the H-h + 1 rows
#so in our case the result will be like this
#result =   [ [1, 1, 1]
             #[]
             #[]]
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)

(minv, maxv, minLoc, maxLoc) = cv2.minMaxLoc(result)
topLeft = maxLoc
botRight = topLeft[0]+w, topLeft[1]+h

print(topLeft,botRight)


#get the roi
verticalSlice = slice(topLeft[1],botRight[1])
horizontalSlice = slice(topLeft[0],botRight[0])
roi = img[verticalSlice, horizontalSlice]

# construct a darkened transparent 'layer' to darken everything
# in the puzzle except for waldo

mask = np.zeros(img.shape, dtype = "uint8")
img = cv2.addWeighted(img, 0.25, mask, 0.75, 0)

# put the original waldo back in the image so that he is
# 'brighter' than the rest of the image

img[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = template
cv2.imshow("Found Waldo", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Using all diff methods")
#another way
for method in methods:
    testimg = img2.copy()
    result = cv2.matchTemplate(testimg, template, method)
    (minv, maxv, minLoc, maxLoc) = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = minLoc
    else:
        location = maxLoc
    botRight = location[0]+w, location[1]+h
    cv2.rectangle(testimg, location, botRight, 255, thickness = 2)
    cv2.imshow("Matched using method " +str(method), testimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

