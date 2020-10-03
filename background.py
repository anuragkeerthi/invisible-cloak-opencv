import cv2

capture = cv2.VideoCapture(2)

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        cv2.imshow("image", frame)
        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite('image.jpg', frame)


capture.release()
cv2.destroyAllWindows()