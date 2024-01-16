import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture("pedestrian.avi")

if not os.path.exists('data'):
    os.makedirs('data')

currentframe = 0
while (True):
    # reading from frame
    ret, frame = cam.read()

    if ret:
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # Write and update images
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break
