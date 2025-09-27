# 🟢 Smart Face Recognition Attendance System

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.7-green?logo=opencv&logoColor=white)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A **Python-based Face Recognition Attendance System** using **OpenCV** and **face_recognition**. Automatically detects faces from images or a webcam and logs attendance in a CSV file with **name, date, and time**.  

---

## ✨ Features

- ✅ Detect and recognize faces in images and webcam  
- ✅ Train the model with multiple images for accurate recognition  
- ✅ Real-time attendance marking  
- ✅ Attendance saved in `Attendance.csv` with timestamp  
- ✅ Highlights detected faces with rectangles and names  
- ✅ Scalable: Add more images to recognize more people  

---

## 🛠️ Installation

1. **Clone the repository:**

>git clone [https://github.com/yourusername/face-recognition-attendance.git](https://github.com/Falcon37-tech/Smart-Face-Recognition-Attendance-System/tree/main)
>cd face-recognition-attendance

2. **Install dependencies:**
>pip install opencv-python numpy face_recognition

>⚠️ Windows users might also need:
>pip install cmake dlib

3. **Prepare folders**
>student_images/
➔ Folder with training images
>Attendance.csv
➔ CSV file to store attendance

## Usage🚀

### Detect Face in Image

>import cv2
>import face_recognition
>img = face_recognition.load_image_file('elon_musk.jpg')
>img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
>face_location = face_recognition.face_locations(img_rgb)[0]
>cv2.rectangle(img, (face_location[3], face_location[0]), (face_location[1], face_location[2]), (255,0,255), 2)
>cv2.imshow('Detected Face', img)
>cv2.waitKey(0)
>cv2.destroyAllWindows()

### Train the Model

- Load images from `student_images/` and encode faces:
>encoded_faces = findEncodings(images)
- The model can now recognise all faces in your dataset.

### Real-Time Attendance
>python face_recognition_attendance.py

## Open your webcam, detect faces, and automatically log attendance in   `Attendance.csv`

### Attendance Format📂
| Name | Time | Date |
| -------- | -------- | -------- |
| Elon Musk | 10:15:23PM | 27-September-2025 |
| John Doe | 11:05:10AM | 27-September-2025 |

### Folder Structure 📂
face-recognition-attendance/
│
├── student_images/                  ➔ Training images
├── Attendance.csv                   ➔ Attendance log
├── face_recognition_attendance.py   ➔ Main script
└── README.md                        ➔ Project documentation

### Notes ⚡

- Use clear, front-facing images for best results
- Webcam index might vary (0 or 1) depending on your system
- Works best in good lighting
- Easily extendable to multiple users or integrated with a GUI 

## **Research Paper:** 📄 
>I’ve added a research paper related to this project—[Reference Paper.pdf](research-paper.pdf) for anyone interested in learning more.

---

## 🙏 Thank You! 🎉✨

Thank you for visiting this project!  
I hope this Face Recognition Attendance System helps you learn and build something amazing.  

💡 **Feel free to explore, contribute, or leave a ⭐ on the repo!**  
