import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.core.base_options import BaseOptions

# Load FaceLandmarker
base_options = BaseOptions(model_asset_path="face_landmarker.task")
options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    num_faces=1,
    output_face_blendshapes=False,
    output_facial_transformation_matrixes=False
)
face_landmarker = vision.FaceLandmarker.create_from_options(options)

# Acupressure landmark indices
acupressure_points = {
    "BL-1": 133,
    "GB-1": 33,
    "ST-1": 145,
    "Yuyao": 65
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    detection = face_landmarker.detect(mp_image)

    if detection.face_landmarks:
        for face_landmarks in detection.face_landmarks:
            h, w, _ = frame.shape

            for name, idx in acupressure_points.items():
                lm = face_landmarks[idx]
                x = int(lm.x * w)
                y = int(lm.y * h)
                cv2.circle(frame, (x, y), 6, (0, 255, 0), -1)
                cv2.putText(frame, name, (x+5, y-5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 255), 1)

    cv2.imshow("Realtime Eye Acupressure Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
