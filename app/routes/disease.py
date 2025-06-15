from flask import Blueprint, jsonify
import json
import os

disease_bp = Blueprint('disease_bp', __name__)

# Dapatkan path absolut ke file diseases.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, '..', 'data', 'diseases.json')

@disease_bp.route('/diseases', methods=['GET'])
def get_all_diseases():
    with open(JSON_PATH) as f:
        diseases = json.load(f)
    return jsonify(diseases)

@disease_bp.route('/diseases/<name>', methods=['GET'])
def get_disease_by_name(name):
    with open(JSON_PATH) as f:
        diseases = json.load(f)

    for disease in diseases:
        if disease['name'].lower().replace(" ", "_") == name.lower().replace(" ", "_"):
            return jsonify(disease)

    return jsonify({'error': 'Penyakit tidak ditemukan'}), 404
