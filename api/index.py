from flask import Flask, request, jsonify
from app.ocr import ModelManager
from absl import logging

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

# Get the image file for assessments 
@app.route('/upload-assessments-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    image_data = modelManager.inference_on_image(file)
    logging.info(f"got image data: {image_data}")
    model_response = modelManager.inference_on_transcript(image_data)

    return jsonify({'message': 'Image uploaded successfully', 'filename': file.filename})

if __name__ == '__main__':
    modelManager = ModelManager()
    app.run(debug=True)
