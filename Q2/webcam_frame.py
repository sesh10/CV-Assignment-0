import cv2
import os

# Create a folder to save the frames
if not os.path.exists('frames'):
    os.makedirs('frames')

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")

currentframe = 0

# Read until video is completed
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow('Frame', frame)
        cv2.imwrite('frames/frame_' + str(currentframe) + '.jpg', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
    currentframe += 1


# When everything done, release the video capture object and close all frames
cap.release()
cv2.destroyAllWindows()