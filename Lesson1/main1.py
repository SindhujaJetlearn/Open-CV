import cv2

img=cv2.imread("pika.png",1)

# There are 3 parameters to read an image - 
#cv2.IMREAD_COLOR (1) => Specify to load the image in color. excludes transaperency
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged

# imshow is used to show the loaded image in a new window with a title
cv2.imshow("Pikachu Image",img)

# To hold the window until the user presses a key on keyboard
cv2.waitKey(0)

# delete / close the image window after the key pressed
cv2.destroyAllWindows()





