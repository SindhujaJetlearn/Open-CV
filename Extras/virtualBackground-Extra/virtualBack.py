import cv2
import numpy as np

p = cv2.imread("p.jpg")


#Step 1 convert to HSV

hsvp = cv2.cvtColor(p, cv2.COLOR_BGR2HSV)
cv2.imshow("Portrait",hsvp)

lower_greens = np.array([45,50,50])
upper_greens = np.array([79,255,255])

maskGreens = cv2.inRange(hsvp, lower_greens, upper_greens)
#invert the maskGreen
maskGreensNot = cv2.bitwise_not(maskGreens)
cv2.imshow("Not Mask", maskGreensNot)


maskedPort = cv2.bitwise_and(p, p, mask=maskGreensNot)

cv2.imshow("Mask Port", maskedPort)
#cv2.imshow("Mask Green", maskGreens)

#copyOrig = p.copy()
#copyOrig[np.where(maskGreens == 255)] = 0

#cv2.imshow("Replacing greens with Black", copyOrig)


#


bg = cv2.imread("bg.jpg")
h,w,c = p.shape

#resizing -
bg = cv2.resize(bg, (w,h))


#we will apply this mask on top of the bg
maskedbg = cv2.bitwise_and(bg,bg, mask = maskGreens)
cv2.imshow("masked background", maskedbg)


#addition
finalimg = cv2.addWeighted(maskedbg, 1, maskedPort, 1, 0 )
cv2.imshow("Final", finalimg)

cv2.waitKey(0)
cv2.destroyAllWindows()
