import cv2

# Read a image using cv
img = cv2.imread("hugh.jpeg")

# Display the image
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Change the color of the image
# BGR to Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Display the image
cv2.imshow("Gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
