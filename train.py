import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam
from model import build_model

IMG_SIZE = 224
DATASET_PATH = '../dataset/train'

def load_data():
    images = []
    labels = []

    classes = {
        "car": 1,
        "no_car": 0
    }

    for class_name, label in classes.items():
        folder = os.path.join(DATASET_PATH, class_name)

        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            img = cv2.imread(path)

            if img is not None:
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                img = img / 255.0
                images.append(img)
                labels.append(label)

    return np.array(images), np.array(labels)

X, y = load_data()

print("Total images:", len(X))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = build_model()
model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size=16)

loss, acc = model.evaluate(X_test, y_test)

print("Accuracy:", acc)

os.makedirs('../model', exist_ok=True)
model.save('../model/resnet_model.h5')