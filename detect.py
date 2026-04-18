from ultralytics import YOLO
import cv2

# ✅ use local file instead of downloading
model = YOLO("yolov8n.pt")

def detect_image(image_path):
    results = model(image_path)

    for r in results:
        if len(r.boxes) > 0:
            img = r.plot()
            cv2.imwrite(image_path, img)
            return "Car Detected 🚗"

    return "No Car ❌"