# 🚗 YOLO-Based Car Detection System

## 📌 Overview

This project presents an **AI-powered car detection system** developed using the **YOLOv8 (You Only Look Once)** object detection algorithm. The system is designed to identify cars in images with high accuracy and speed. It integrates deep learning with a **Flask-based web application**, allowing users to upload images and instantly receive detection results.

The main goal of this project is to demonstrate the practical implementation of **computer vision and deep learning** techniques in solving real-world problems such as traffic monitoring, surveillance, and smart city applications.

___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

## 🎯 Features

* 🚗 **Car Detection using YOLOv8**
* 📤 **Image Upload via Web Interface**
* ⚡ **Fast and Real-Time Detection**
* 🎨 **User-Friendly Interface**
* 📦 **Bounding Box Visualization**



## 🧠 Technologies Used

### 🔹 Programming Language

* **Python 3.x**

### 🔹 Libraries & Frameworks

* **YOLOv8 (Ultralytics)**
* **Flask**
* **OpenCV**
* **NumPy**

### 🔹 Frontend

* **HTML, CSS, Bootstrap**



## 📊 Dataset

The dataset used in this project is sourced from Kaggle:

🔗 https://www.kaggle.com/datasets/sshikamaru/car-object-detection

### 📌 Description

* Contains images of cars from multiple angles
* Includes annotations for object detection
* Suitable for training and testing YOLO models

### 📥 How to Use

1. Download the dataset from the above link
2. Extract the ZIP file
3. Place it inside your project folder:


## ⚙️ Installation Guide

### 1️⃣ Clone Repository


git clone https://github.com/YOUR_USERNAME/yolo-car-detection-webapp.git
cd yolo-car-detection-webapp


### 2️⃣ Install Dependencies

pip install ultralytics flask opencv-python

## ▶️ How to Run the Project

### Step 1:


python app.py


### Step 2:

Open in browser:
http://127.0.0.1:5000/

### Step 3:

* Upload an image
* Click **Detect Now**
* View detection result



## 📸 Output

* Detects cars in uploaded images
* Displays result with bounding boxes
* Shows detection status (Car / No Car)


## 🔍 Working Principle

1. User uploads an image
2. Image is processed by YOLO model
3. Objects are detected in a single pass
4. If car is found:

   * Bounding box is drawn
   * Result is displayed
5. Output shown on web interface



## 🚀 Future Scope

* 🎥 Real-time video detection
* 🚦 Multi-object detection
* 📱 Mobile application integration
* 🌆 Smart traffic systems
* ⚡ Model optimization
* 📊 Analytics dashboard


## 👨‍💻 Author

**Khushi Kaduskar**

This project is developed as part of academic coursework to demonstrate the application of **deep learning and computer vision techniques** in real-world scenarios.
