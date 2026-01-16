# 👁️ Eye Acupressure Realtime Detection

A realtime computer vision application that detects facial landmarks from a webcam feed and displays eye acupressure points on both eyes with automatic zoom-in and smooth tracking.

This project uses **MediaPipe Face Landmarker (Tasks API)** and **OpenCV** to provide a clean and responsive visual guide for eye acupressure.

---

## ✨ Features

* Realtime face detection using MediaPipe FaceLandmarker
* Automatic zoom-in to the detected face
* Smooth zoom transition (anti-jitter smoothing)
* Detection of **10 main eye acupressure points** (5 on each eye)
* Clean visualization (no labels, only points)
* Automatically exits when the camera window is closed
* Lightweight and runs on CPU

---

## 📍 Acupressure Points

Each eye uses 5 main points:

* **BL-1** – Inner eye corner
* **GB-1** – Outer eye corner
* **ST-1** – Lower eye area
* **Yuyao** – Middle of eyebrow
* **Taiyang** – Temple

Total: **10 points (Left + Right eye)**

---

## 🧠 Technology Stack

* Python 3.9+
* MediaPipe Tasks API (Face Landmarker)
* OpenCV
* NumPy

---

## 📁 Project Structure

```
eye_acupressure/
│── eye_acupressure_realtime.py
│── face_landmarker.task
│── README.md
│── requirements.txt
│── venv/
```

---

## ⚙️ Installation

### 1. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 2. Install Dependencies Using requirements.txt

All required libraries are listed in `requirements.txt`.

Run the following command inside the project folder:

```bash
pip install -r requirements.txt
```

This command will automatically install:

* mediapipe
* opencv-python
* numpy

---

### 3. Download FaceLandmarker Model

Download the FaceLandmarker model from:

[https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/latest/face_landmarker.task](https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/latest/face_landmarker.task)

After downloading, place the file in the project root folder:

```
eye_acupressure/face_landmarker.task
```

---

## ▶️ Running the Application

After completing installation, run the program using:

```bash
python eye_acupressure_realtime.py
```

### How to Use

* Look directly at the webcam
* The camera will automatically zoom in on your face
* Green dots will appear on the eye acupressure points
* Close the window or press `ESC` to exit

---

## ⚠️ Disclaimer

This application is for **educational and visualization purposes only**.
It is **not a medical device** and should not be used for diagnosis or treatment.

---

## 🚀 Future Improvements

* Finger detection to verify correct pressing
* Timer per acupressure point
* Audio or visual guidance
* Data logging for user sessions
* Mobile integration (Flutter)

---

## 👨‍💻 Author

**Muhammad Iqbal Saputra**
Universitas Harkat Negeri – Informatics Engineering

---

## 📜 License
