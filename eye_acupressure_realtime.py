import cv2
import mediapipe as mp
import numpy as np
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

# 10 titik akupresur
acupressure_points = {
    "R_BL1": 133, "R_GB1": 33, "R_ST1": 145, "R_Yuyao": 65, "R_Taiyang": 246,
    "L_BL1": 362, "L_GB1": 263, "L_ST1": 374, "L_Yuyao": 295, "L_Taiyang": 466
}

cap = cv2.VideoCapture(0)

prev_bbox = None
alpha = 0.2  # smoothing factor (lebih kecil = lebih halus)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    detection = face_landmarker.detect(mp_image)

    display_frame = frame.copy()

    if detection.face_landmarks:
        face_landmarks = detection.face_landmarks[0]

        xs = np.array([lm.x * w for lm in face_landmarks])
        ys = np.array([lm.y * h for lm in face_landmarks])

        x1, x2 = xs.min(), xs.max()
        y1, y2 = ys.min(), ys.max()

        # margin lebih kecil agar zoom lebih dekat
        margin_x = (x2 - x1) * 0.1
        margin_y = (y2 - y1) * 0.1

        target_bbox = np.array([
            max(x1 - margin_x, 0),
            max(y1 - margin_y, 0),
            min(x2 + margin_x, w),
            min(y2 + margin_y, h)
        ])

        if prev_bbox is None:
            prev_bbox = target_bbox

        # Smooth transition
        prev_bbox = alpha * target_bbox + (1 - alpha) * prev_bbox
        x1s, y1s, x2s, y2s = prev_bbox.astype(int)

        face_crop = frame[y1s:y2s, x1s:x2s]
        if face_crop.size > 0:
            display_frame = cv2.resize(face_crop, (w, h))

            crop_h, crop_w, _ = face_crop.shape
            for name, idx in acupressure_points.items():
                lm = face_landmarks[idx]
                x = int((lm.x * w - x1s) * w / crop_w)
                y = int((lm.y * h - y1s) * h / crop_h)
                cv2.circle(display_frame, (x, y), 6, (0,255,0), -1)
                cv2.putText(display_frame, name, (x+5, y-5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255,255), 1)

    cv2.imshow("Eye Acupressure Auto Zoom Smooth", display_frame)

    if cv2.getWindowProperty("Eye Acupressure Auto Zoom Smooth", cv2.WND_PROP_VISIBLE) < 1:
        break

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
