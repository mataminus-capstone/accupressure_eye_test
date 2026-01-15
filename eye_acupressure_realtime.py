from mediapipe.tasks.python.core.base_options import BaseOptions
from mediapipe.tasks.python import vision
import mediapipe as mp
import cv2
acupressure_points = {
    # Mata kanan (dari sudut pandang user)
    "R_BL1": 133,
    "R_GB1": 33,
    "R_ST1": 145,
    "R_Yuyao": 65,
    "R_Taiyang": 246,

    # Mata kiri
    "L_BL1": 362,
    "L_GB1": 263,
    "L_ST1": 374,
    "L_Yuyao": 295,
    "L_Taiyang": 466
}


# Load FaceLandmarker
base_options = BaseOptions(model_asset_path="face_landmarker.task")
options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    num_faces=1,
    output_face_blendshapes=False,
    output_facial_transformation_matrixes=False
)
face_landmarker = vision.FaceLandmarker.create_from_options(options)

# 10 Titik akupresur (5 kiri, 5 kanan)
acupressure_points = {
    "R_BL1": 133, "R_GB1": 33, "R_ST1": 145, "R_Yuyao": 65, "R_Taiyang": 246,
    "L_BL1": 362, "L_GB1": 263, "L_ST1": 374, "L_Yuyao": 295, "L_Taiyang": 466
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
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
                cv2.putText(frame, name, (x+4, y-4),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1)

    cv2.imshow("Eye Acupressure Guide", frame)

    # Jika window ditutup manual → keluar
    if cv2.getWindowProperty("Eye Acupressure Guide", cv2.WND_PROP_VISIBLE) < 1:
        break

    # ESC juga bisa keluar
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
