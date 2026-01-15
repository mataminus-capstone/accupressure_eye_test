# 🛠 Cara Install Eye Acupressure Realtime Detection

Panduan ini menjelaskan langkah-langkah instalasi dan menjalankan aplikasi **Eye Acupressure Realtime Detection** di komputer lokal.

---

## 📌 Persyaratan

Pastikan sudah terinstall:

- Python **3.9 atau lebih baru**
- Git (opsional)
- Webcam aktif

Cek Python:

```bash
python --version
````

---

## 📁 1. Clone atau Download Project

Jika menggunakan Git:

```bash
git clone <repository_url>
cd eye_acupressure
```

Atau download ZIP lalu ekstrak ke folder.

---

## 🧪 2. Buat Virtual Environment (Disarankan)

```bash
python -m venv venv
```

Aktifkan environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

---

## 📦 3. Install Dependency

Pastikan berada di folder project lalu jalankan:

```bash
pip install -r requirements.txt
```

---

## 📥 4. Download Model FaceLandmarker

Download file berikut:

[https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/latest/face_landmarker.task](https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/latest/face_landmarker.task)

Simpan ke folder project:

```
eye_acupressure/face_landmarker.task
```

---

## ▶️ 5. Jalankan Aplikasi

```bash
python eye_acupressure_realtime.py
```

---

## 🎯 Cara Menggunakan

1. Hadapkan wajah ke webcam
2. Kamera akan otomatis zoom ke wajah
3. Titik hijau menunjukkan titik akupresur mata
4. Tutup window atau tekan ESC untuk keluar

---

## ⚠️ Troubleshooting

### Webcam tidak muncul

* Pastikan webcam tidak dipakai aplikasi lain
* Coba ganti index kamera:

  ```python
  cap = cv2.VideoCapture(1)
  ```

### Titik tidak muncul

* Pastikan wajah menghadap kamera
* Cahaya cukup
* Pastikan file `face_landmarker.task` ada

### Error module not found

Jalankan:

```bash
pip install -r requirements.txt
```

---

## 📜 Catatan

Aplikasi ini hanya untuk tujuan edukasi dan visualisasi, bukan alat medis.

---

Selesai 🎉

```

---

## 📁 Struktur Akhir

```

eye_acupressure/
│── eye_acupressure_realtime.py
│── face_landmarker.task
│── README.md
│── carainstall.md
│── requirements.txt
│── venv/

```
