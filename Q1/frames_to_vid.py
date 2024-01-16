import cv2
import os
from os.path import isfile, join

# Read the images from the directory
path = 'data/'
images = [f for f in os.listdir(path) if isfile(join(path, f))]
images.sort(key = lambda x: int(x[5:-4]))

video_frames = []

for i in range(len(images)):
    images[i] = path + images[i]
    img = cv2.imread(images[i])
    height, width, layers = img.shape
    size = (width, height)
    if img is not None:
        video_frames.append(img)

# Specify the frame rate
fps = float(input("Enter frame rate: "))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, fps, size)

# Display the video
print(len(video_frames))
for i in range(len(video_frames)):
    out.write(video_frames[i])
    cv2.imshow('video', video_frames[i])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()
