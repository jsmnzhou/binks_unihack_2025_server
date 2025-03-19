from flask import Flask, request, jsonify
import os
from supabase import create_client, Client

app = Flask(__name__)

SUPABASE_URL = "https://your-supabase-url.supabase.co"
SUPABASE_KEY = "your-supabase-api-key"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

# Get the image file
@app.route('/upload-assessments-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    save_path = os.path.join('uploads', file.filename)
    os.makedirs('uploads', exist_ok=True)
    file.save(save_path)
    return jsonify({'message': 'Image uploaded successfully', 'filename': file.filename})

# API to create a class entry in Supabase
@app.route('/create-assessment', methods=['POST'])
def create_assessment():
    data = request.get_json()
    class_name = data.get('class_name')
    if not class_name:
        return jsonify({'error': 'class_name is required'}), 400

    response = supabase.table('class').insert({'class_name': class_name}).execute()
    if response.status_code != 201:
        return jsonify({'error': 'Failed to insert into Supabase', 'details': response.data}), 500

    return jsonify({'message': 'Class created successfully', 'data': response.data}), 201

