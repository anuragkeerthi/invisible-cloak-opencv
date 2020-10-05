# Another Approach

import numpy as np
import cv2
import time

capture = cv2.VideoCapture(0)

time.sleep(3)

background = 0

for i in range(30):
    ret, background = capture.read()

while capture.isOpened():
    ret, image = capture.read()

    if not ret:
        break

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_limit_color = np.array([0,120,70])
    upper_limit_color = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_limit_color, upper_limit_color) # Separating the Cloak

    lower_limit_color = np.array([170,120,70])
    upper_limit_color = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, lower_limit_color, upper_limit_color) # For Another shade of Red

    mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=2) # To remove Noise

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations=1) # Smoothing the image

    mask2 = cv2.bitwise_not(mask1)

    result1 = cv2.bitwise_and(background, background, mask = mask1) # Used for Segmentation of the Color
    result2 = cv2.bitwise_and(image,image, mask = mask2) # Used to Substitute the Cloak part

    final_output = cv2.addWeighted(result1, 1, result2, 1, 0)

    cv2.imshow("Cloak", final_output)

    if cv2.waitKey(5) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

