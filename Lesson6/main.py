#Refer - https://www.geeksforgeeks.org/python-create-video-using-multiple-images-using-opencv/
#remove ouput video before running the program
#Create a Video Collage (Video created out of images)
#pip install Pillow

import os
import cv2
from PIL import Image 
#Pillow - Image Processing Library Python Imaging Library

#Change the directory as per own folder path where the images are located
os.chdir('C:/Users/HP/Desktop/JL/OpenCV/Lesson6/photos')
path = 'C:/Users/HP/Desktop/JL/OpenCV/Lesson6/photos'

mean_height = 0
mean_width = 0

#os.listdir('.') - to list files and directories in a current working directory
num_of_images = len(os.listdir('.')) 
print("Number of images:",num_of_images)

for file in os.listdir('.'):
    #os.path.join() function allows you to join one or more path segments 
    #to create a complete path.
    #C:/Users/HP/Desktop/JL/OpenCV/Lesson6/photos/one.jpg
    img=Image.open(os.path.join(path,file))
    width, height = img.size
    mean_width = mean_width + width
    mean_height = mean_height + height

mean_width=mean_width//num_of_images
mean_height=mean_height//num_of_images

print("Mean Width : ",mean_width)
print("Mean Height : ",mean_height)


for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        img = Image.open(os.path.join(path, file))
        imgResized = img.resize((mean_width, mean_height))
        imgResized.save(file, 'JPEG', quality = 100)
        print("Image is resized")

def videoGenerator(): 
    video_name = "MyFirstVideo.avi"
    os.chdir('C:/Users/HP/Desktop/JL/OpenCV/Lesson6/photos')
    images=[]
    for img in os.listdir('.'):
        if img.endswith('.jpg') or img.endswith('.jpeg') or img.endswith('.png'):
            images.append(img)
    print(images)

    #setting the frame width, height of first image (coz all image will be of same size)
    frame = cv2.imread(os.path.join(".", images[0]))
    
    #layer - 3 for RGB and 1 for grayscale image
    height, width,layer = frame.shape

    print(frame.shape)

    #fourcc is a four-character code that specifies the video codec to use.
    #cv2.VideoWriter(filename, fourcc,fps, frameSize)
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    #Appending the images to the video one by one
    for image in images:
        video.write(cv2.imread(os.path.join(".", image)))

    cv2.destroyAllWindows()
    video.release()  

videoGenerator()




