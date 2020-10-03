import cv2
import numpy as np 

capture = cv2.VideoCapture(0)
background_image = cv2.imread('./image.png')

while capture.isOpened():
    ret, frame = capture.read()
    
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv", hsv)

        if cv2.waitKey(5) == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()
