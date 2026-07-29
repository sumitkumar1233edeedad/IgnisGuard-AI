# 🔥 IgnisGuard AI

IgnisGuard AI is a real-time Fire and Smoke Detection web application built using **Django** and **YOLOv8**. The system detects fire and smoke from uploaded images and videos using a custom-trained deep learning model. The project provides a simple web interface where users can upload media and instantly receive AI-powered detection results.

This project is designed to demonstrate the practical use of Computer Vision and Deep Learning for improving fire safety and early hazard detection.

---

## 🚀 Features

- 🔥 Fire Detection
- 💨 Smoke Detection
- 📷 Image Detection
- 🎥 Video Detection
- 🤖 YOLOv8 Object Detection
- 🌐 Responsive Web Interface
- ⚡ Fast AI Predictions
- 📱 User-Friendly Design

---

## 🛠️ Technologies Used

### Backend
- Python
- Django

### AI / Machine Learning
- YOLOv8 (Ultralytics)
- OpenCV
- NumPy

### Frontend
- HTML5
- CSS3
- JavaScript

### Dataset
- Custom Fire & Smoke Dataset
- Dataset Created and Managed using **Roboflow**

---

## 🧠 Model

The detection model is trained using **YOLOv8** on a custom dataset created with **Roboflow**. The model is capable of identifying:

- Fire
- Smoke

The trained model is integrated into Django for real-time inference.

---

## 📂 Project Structure

```
IgnisGuard-AI/
│
├── dectector/
├── templates/
├── static/
├── media/
├── models/
│   └── best.pt
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/sumitkumar1233edeedad/IgnisGuard-AI.git

cd IgnisGuard-AI
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

Windows

```bash
env\Scripts\activate
```

Linux / macOS

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Server

```bash
python manage.py migrate

python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

Add screenshots here.

```
Home Page

Detection Page

Prediction Result
```

---

## 📊 Dataset

The model was trained using a **custom Fire and Smoke dataset** created with **Roboflow**.

Dataset includes:

- Fire Images
- Smoke Images
- Annotated Bounding Boxes
- Multiple Real-World Scenarios

---

## 🎯 Future Improvements

- Live Webcam Detection
- CCTV Camera Integration
- Email Alert System
- SMS Notifications
- Cloud Deployment
- Mobile-Friendly Dashboard

---

## 👨‍💻 Author

**Sumit Kumar**

AI/ML Developer

GitHub: https://github.com/sumitkumar1233edeedad

LinkedIn: **

---

## 📜 License

This project is created for educational and portfolio purposes.
