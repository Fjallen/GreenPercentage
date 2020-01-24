import cv2
import numpy as np

# Load Image
img = cv2.imread("1.jpg") # File Name Here

# convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# mask of green (36,25,25) ~ (86, 255,255), but you can choose
mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255)) # Tweek your mask filter here

# slice the green
imask = mask>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

# Get a count of pixels masked
count = 0
for col in imask:
	for point in col:
		if (point==True):
			count+=1

# Get number of pixels divided by area in decimal
print(count / (mask.shape[0] * mask.shape[1])) # Basically percentage of green pixels in image

# Save the image with mask
cv2.imwrite("output.jpg", green)