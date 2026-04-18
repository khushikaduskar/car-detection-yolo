import os
import shutil
import cv2
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Load pretrained model
model = ResNet50(weights='imagenet')

SOURCE = r"F:\sl2_mp\dataset\mixed"
CAR_FOLDER = r"F:\sl2_mp\dataset\train\car"
NO_CAR_FOLDER = r"F:\sl2_mp\dataset\train\no_car"

os.makedirs(CAR_FOLDER, exist_ok=True)
os.makedirs(NO_CAR_FOLDER, exist_ok=True)

# Keywords for car detection
car_keywords = ["car", "cab", "taxi", "jeep", "limousine", "sports_car", "minivan"]

for file in os.listdir(SOURCE):
    path = os.path.join(SOURCE, file)

    try:
        img = image.load_img(path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        decoded = decode_predictions(preds, top=3)[0]

        labels = [label for (_, label, _) in decoded]

        if any(word in label for label in labels for word in car_keywords):
            shutil.copy(path, os.path.join(CAR_FOLDER, file))
            print(f"{file} → CAR")
        else:
            shutil.copy(path, os.path.join(NO_CAR_FOLDER, file))
            print(f"{file} → NO CAR")

    except:
        print(f"Skipping {file}")

print("✅ Auto sorting completed!")