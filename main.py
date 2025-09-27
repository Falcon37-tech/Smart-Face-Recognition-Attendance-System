# For Wevcam Recognition & Attendance

import cv2
import numpy as np
import face_recognition
from face_utils import load_image_rgb, find_face_locations, encode_face
from attendance import markAttendance
from train import load_images_from_folder, findEncodings

# Load training data
path = 'student_images'
images, classNames = load_images_from_folder(path)
encoded_face_train = findEncodings(images)

# Start webcam
cap = cv2.VideoCapture(0)  # 0 = default camera
if not cap.isOpened():
    print("❌ Could not open the camera. Check connection or index.")
    exit()

while True:
    success, img = cap.read()
    if not success or img is None:
        continue

    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

    for encode_face_curr, faceloc in zip(encoded_faces, faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face_curr)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face_curr)
        matchIndex = np.argmin(faceDist)
        
        if matches[matchIndex]:
            name = classNames[matchIndex]
            y1, x2, y2, x1 = [v*4 for v in faceloc]  # Scale back
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0,255,0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-5), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            markAttendance(name)

    cv2.imshow('External Camera', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
