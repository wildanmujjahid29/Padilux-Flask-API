import os
from tensorflow.keras.models import load_model

def load_trained_model():
    model_path = os.path.join("model", "rice_leaf_mobilenetv2.h5")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}")
    return load_model(model_path)
