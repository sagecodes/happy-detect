import cv2

# load Cascade(s) for face and feature detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# Detect face and draw rectangle around region of interest in original image
# you may need to adjust scaling factor and minimum num of neighbors
# depending on your camera setup for accurate smile detection
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) 
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = frame[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 23)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color,(sx, sy),(sx+sw, sy+sh), (0, 255, 0), 2)
    return frame

# open webcam for video capture | try changing 0 to 1 for external webcam
# convert to gray for cascades
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
