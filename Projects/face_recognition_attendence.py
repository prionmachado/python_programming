import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os

# ✅ Function to load image and convert to RGB safely
def load_image_rgb_cv2(path):
    img_bgr = cv2.imread(path)
    if img_bgr is None:
        raise FileNotFoundError(f"Failed to read image from {path}")
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return img_rgb

# ✅ Auto-load known faces from folder
def load_known_faces(folder_path):
    known_encodings = []
    known_names = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            name = os.path.splitext(filename)[0]  # Name from filename
            path = os.path.join(folder_path, filename)
            try:
                image = load_image_rgb_cv2(path)
                encodings = face_recognition.face_encodings(image)
                if not encodings:
                    print(f"⚠️ No face found in {filename}, skipping.")
                    continue
                known_encodings.append(encodings[0])
                known_names.append(name)
                print(f"✅ Loaded and encoded: {filename}")
            except Exception as e:
                print(f"❌ Error loading {filename}: {e}")

    return known_encodings, known_names

# ✅ Load all known faces from folder
known_face_encodings, known_face_names = load_known_faces("Projects/known_faces")

# ✅ Ensure we loaded at least one face
if not known_face_encodings:
    raise RuntimeError("❌ No valid face images found in 'Projects/known_faces'.")

# Track attendance
students = known_face_names.copy()
face_locations = []
face_encodings = []

# Setup attendance file
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
f = open(f"attendance_{current_date}.csv", "w+", newline='')
lnwriter = csv.writer(f)
lnwriter.writerow(["Name", "Time"])

# Start webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to grab frame")
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        name = "Unknown"
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            top, right, bottom, left = face_location
            top *= 4; right *= 4; bottom *= 4; left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name + " Present", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            if name in students:
                students.remove(name)
                current_time = datetime.now().strftime("%H:%M:%S")
                lnwriter.writerow([name, current_time])
                print(f"{name} marked present at {current_time}")

    cv2.imshow("Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
