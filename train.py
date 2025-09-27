# For Encode Training images

import cv2
import os
from face_utils import load_image_rgb, encode_face

def load_images_from_folder(path):
    """Load all images and return image array & class names."""
    images = []
    classNames = []
    for filename in os.listdir(path):
        img = cv2.imread(f'{path}/{filename}')
        if img is not None:
            images.append(img)
            classNames.append(os.path.splitext(filename)[0])
    return images, classNames

def findEncodings(images):
    """Return list of encoded faces from images."""
    encodeList = []
    for img in images:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodeList.append(encode_face(img_rgb))
    return encodeList

if __name__ == "__main__":
    path = 'student_images'
    images, classNames = load_images_from_folder(path)
    encoded_faces = findEncodings(images)
    print(f"[INFO] Training completed for {len(classNames)} people: {classNames}")
