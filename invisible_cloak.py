import cv2
import numpy as np 

capture = cv2.VideoCapture(0)
background_image = cv2.imread('./image.png')

while capture.isOpened():
    ret, frame = capture.read()
    
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv", hsv)
        rgb_colour = np.unit8([[[0,0,255]]])
        hsv_colour = cv2.cvtColor(rgb_colour, cv2.COLOR_BGR2HSV)

        if cv2.waitKey(5) == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()
