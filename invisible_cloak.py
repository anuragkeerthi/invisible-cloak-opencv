import cv2
import numpy as np 

capture = cv2.VideoCapture(0)
background_image = cv2.imread('./image.jpg')

while capture.isOpened():
    ret, frame = capture.read()
    
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv", hsv)
        rgb_color = np.uint8([[[0,0,255]]]) #Insert any color
        hsv_color = cv2.cvtColor(rgb_color, cv2.COLOR_BGR2HSV)

        lower_threshold_color = np.array([0,100,100])
        higher_threshold_color = np.array([10,255,255])

        mask = cv2.inRange(hsv, lower_threshold_color, higher_threshold_color)
        #cv2.imshow("mask", mask)

        replace_background = cv2.bitwise_and(background_image,background_image, mask=mask)
        #cv2.imshow("replace_background", replace_background)

        mask = cv2.bitwise_not(mask)

        replace_frame = cv2.bitwise_and(frame, frame, mask=mask)
        #cv2.imshow("mask", replace_frame)

        cv2.imshow("cloak", replace_background + replace_frame)

        if cv2.waitKey(5) == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()
