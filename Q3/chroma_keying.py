import os
import cv2
import numpy as np
from os.path import isfile, join

# Input video 1 and video 2
video1 = cv2.VideoCapture('person.mp4')
# video1 = cv2.VideoCapture('trex.mp4')
video2 = cv2.VideoCapture('pedestrian.avi')

# Create directories
if not os.path.exists('person_frames'):
    os.makedirs('person_frames')
if not os.path.exists('bg_frames'):
    os.makedirs('bg_frames')
if not os.path.exists('final_frames'):
    os.makedirs('final_frames')

currentframe_person = 0
while True:
    ret, frame = video1.read()

    if ret:
        name = './person_frames/frame' + str(currentframe_person) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)
        currentframe_person += 1
    else:
        break

currentframe_bg = 0
while True:
    ret, frame = video2.read()

    if ret:
        name = './bg_frames/frame' + str(currentframe_bg) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)
        currentframe_bg += 1
    else:
        break


total_frames = min(currentframe_person, currentframe_bg)

# Chroma keying
for i in range(total_frames):
    person_frame = cv2.imread('./person_frames/frame' + str(i) + '.jpg')
    bg_frame = cv2.imread('./bg_frames/frame' + str(i) + '.jpg')

    # Resize bg_frame to 640x480
    bg_frame = cv2.resize(bg_frame, (640, 480))
    person_frame = cv2.resize(person_frame, (640, 480))

    # Convert to HSV
    person_frame_hsv = cv2.cvtColor(person_frame, cv2.COLOR_BGR2HSV)
    bg_frame_hsv = cv2.cvtColor(bg_frame, cv2.COLOR_BGR2HSV)

    # Define range of gray color in HSV
    lower_gray = np.array([0, 0, 0])
    upper_gray = np.array([179, 255, 125])

    # Threshold the HSV image to get only gray colors
    mask = cv2.inRange(person_frame_hsv, lower_gray, upper_gray).astype(np.uint8)

    # Bitwise-AND mask and original image, apply inverse
    res = cv2.bitwise_and(person_frame, person_frame, mask=mask)
    mask_inv = cv2.bitwise_not(mask)
    res2 = cv2.bitwise_and(bg_frame, bg_frame, mask=mask_inv)

    # Add both the images and save
    final = cv2.add(res, res2)
    cv2.imwrite('./final_frames/frame' + str(i) + '.jpg', final)


# Read the images from the directory
path = 'final_frames/'
images = [f for f in os.listdir(path) if isfile(join(path, f))]
images.sort(key = lambda x: int(x[5:-4]))

video_frames = []
size = (640, 480)
for i in range(len(images)):
    images[i] = path + images[i]
    img = cv2.imread(images[i])
    height, width, layers = img.shape
    size = (width, height)
    if img is not None:
        video_frames.append(img)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30, size)

# Display the video
for i in range(len(video_frames)):
    out.write(video_frames[i])
    cv2.imshow('video', video_frames[i])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()