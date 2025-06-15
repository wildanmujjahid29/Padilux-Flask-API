from flask import Blueprint, request, jsonify
from tensorflow.keras.preprocessing import image
import numpy as np
from utils.model_loader import load_trained_model
import os
from werkzeug.utils import secure_filename

predict_bp = Blueprint('predict', __name__)
model = load_trained_model()

class_labels = [
    "Bacterial Leaf Blight",
    "Rice Hispa",
    "Leaf Blast",
    "Leaf scald",
    "Narrow Brown Leaf Spot",
    "Brown Spot",
    "Sheath Blight",
    "Healthy Rice Leaf"
]

@predict_bp.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save image temporarily
    filename = secure_filename(file.filename)
    upload_dir = 'uploads'
    os.makedirs(upload_dir, exist_ok=True)
    filepath = os.path.join(upload_dir, filename)
    file.save(filepath)

    try:
        img = image.load_img(filepath, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        pred = model.predict(img_array)
        class_idx = np.argmax(pred[0])
        confidence = float(pred[0][class_idx])
        predicted_label = class_labels[class_idx]

        return jsonify({
            'prediction': predicted_label,
            'confidence': round(confidence * 100, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)
