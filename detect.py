import cv2

# load Cascade(s) for face and feature detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

def detect():
    return

# open webcam for video capture | try changing 0 to 1 for external webcam
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
