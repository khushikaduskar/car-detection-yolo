from tensorflow.keras.models import load_model
from utils.preprocess import preprocess_image

model = load_model('model/resnet_model.h5')

def predict(path):
    img = preprocess_image(path)
    pred = model.predict(img)

    if pred[0][0] > 0.7:
        return "Car Detected 🚗"
    else:
        return "No Car ❌"