#For VS Code

import cv2
import numpy as np
import face_recognition

#<--------Converting BGR to RGB----------->

'''
After importing libraries you need to load an image.
face_recognition library loads images in the form of BGR, in order to
print the image you should convert it into RGB using OpenCV.
'''

imgelon_bgr = face_recognition.load_image_file('E:\Projects\Face Recognition\elon_musk.jpg')
imgelon_rgb = cv2.cvtColor(imgelon_bgr,cv2.COLOR_BGR2RGB)
cv2.imshow('bgr', imgelon_bgr)
cv2.imshow('rgb', imgelon_rgb)
cv2.waitKey(0)

#<--------Loading image----------->

imgelon = face_recognition.load_image_file('E:\Projects\Face Recognition\elon_musk.jpg')
imgelon = cv2.cvtColor(imgelon,cv2.COLOR_BGR2RGB)

#<--------Finding face location for drawing rectangle----------->

face = face_recognition.face_locations(imgelon)[0]
copy = imgelon.copy()

#<---------Drawing rectangle around the face------------->

'''
You need to draw a bounding box around the faces in order,
to show if the human face has been detected or not.
'''

cv2.rectangle(copy,(face[3], face[0]),(face[1], face[2]),(255,0,255), 2)
cv2.imshow('copy', copy)
cv2.imshow('elon', imgelon)
cv2.waitKey(0)

# <----------------Train an image for face recognition------------------>

'''
Train an image for face recognition
'''

train_elon_encodings = face_recognition.face_encodings(imgelon)[0]

# <----------------Test an image for face recognition------------------>

'''
Test an image for face recognition
'''

test = face_recognition.load_image_file('E:\Projects\Face Recognition\elon_musk_2.jpg')
test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
test_encode = face_recognition.face_encodings(test)[0]
print(face_recognition.compare_faces([train_elon_encodings],test_encode))


# <------------------Building a Face Recognition Model--------------------->

import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import pickle

#<---------------Define a folder path where your training image dataset will be stored------------------->

path = 'E:\Projects\Face Recognition\student_images'

'''
For example: as you see in my student_images path, I have 6 persons. hence our model can recognize only these 6 persons.
you can add more pictures in this directory for more people to be recognized.
'''

#<----------------Create a list to store person_name and image array---------------------------->

'''
Traverse all image files present in the path directory, read images,
and append the image array to the image list and file name to classNames.
''' 

images = []
classNames = []
mylist = os.listdir(path)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

#<-------------------Create a function to encode all the train images and store them in a variable encoded_face_train---------------->

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList
encoded_face_train = findEncodings(images)

#<--------------------Create a function that will create a Attendance.csv file to store the attendance with time---------------------------->

def markAttendance(name):
    with open('E:\Projects\Face Recognition\Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'{name}, {time}, {date}\n')



#<------------------Access the webcam and recognize the face------------------>
'''
With Open('filename.csv', 'r+') create a file and 'r+' mode is used to open a filed for read and write both!
We first check if the name of the attendee is already available in attendance.csv. We won’t write attendance again.
If the attendance’s name is not available in attendance.csv we will write the attendee’s name with a time of function call.
'''

# take pictures from webcam 
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ Could not open the camera. Check connection or index.")
    exit()

while True:
    success, img = cap.read()
    
    # Safety check: skip if no frame received
    if not success or img is None:
        print("⚠️ No frame received. Check camera connection.")
        continue
    
    # Resize and convert to RGB
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    # Detect faces
    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
    
    for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        matchIndex = np.argmin(faceDist)
        
        if matches[matchIndex]:
            name = classNames[matchIndex].upper().lower()
            y1, x2, y2, x1 = faceloc
            # scale back to original size
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            
            # Draw rectangle and label
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-5), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            
            # Mark attendance
            markAttendance(name)
    
    # Show the webcam feed
    cv2.imshow('External Camera', img)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
