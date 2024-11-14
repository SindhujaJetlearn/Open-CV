import cv2

carvpath = cv2.VideoCapture('C:/Users/HP/Desktop/JL/OpenCV/Lesson10/cars.mp4')
caars = cv2.CascadeClassifier('C:/Users/HP/Desktop/JL/OpenCV/Lesson10/carplate.xml')

while True:
    ret, frames = carvpath.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    car = caars.detectMultiScale(gray, 1.1, 1)
    for (x,y,w,z) in car:
        cv2.rectangle(frames, (x, y), (x + w, y + z), (255, 0, 0), 2) #looking for carplate

    # Display frames in a window
    cv2.imshow('video2', frames)
	
	# Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break

# De-allocate any associated memory usage
cv2.destroyAllWindows()

