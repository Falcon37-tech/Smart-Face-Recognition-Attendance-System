# Contain All Face-Related Functions:

import cv2
import face_recognition

def load_image_rgb(path):
    """Load an image and convert BGR to RGB."""
    img = face_recognition.load_image_file(path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def find_face_locations(img):
    """Return face locations in an image."""
    return face_recognition.face_locations(img)

def draw_rectangle(img, faceloc, color=(255,0,255)):
    """Draw rectangle around the face."""
    y1, x2, y2, x1 = faceloc
    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    return img

def encode_face(img):
    """Return face encoding for an image."""
    return face_recognition.face_encodings(img)[0]
