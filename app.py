from flask import Flask, request, jsonify, render_template
from PIL import Image
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os

app = Flask(__name__)

# Load pre-trained model from TensorFlow Hub
MODEL_URL = "https://tfhub.dev/google/imagenet/inception_v3/classification/5"
model = hub.load(MODEL_URL)


LABELS_FILE = "imagenet-classes.txt"
with open(LABELS_FILE, "r") as f:
    labels = f.read().splitlines()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Get the uploaded file
        file = request.files['image']
        if not file:
            return jsonify({"error": "No file uploaded."}), 400

        # Process the image
        image = Image.open(file).resize((299, 299))  # Resize to InceptionV3 input size
        image = np.array(image) / 255.0  # Normalize pixel values
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        image = image.astype(np.float32)  # Ensure the dtype is float32

        # Predict using the model
        predictions = model(image)
        predicted_class = np.argmax(predictions.numpy()[0])
        description = labels[predicted_class]

        return jsonify({"description": description})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)