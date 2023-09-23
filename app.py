# Import necessary Python modules
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, jsonify
import os
import time
import json

# Import custom modules
from modules.open_cv_video_editor import VideoEditor
from modules.image_editor import ImageProcessor
from modules.speach_recognizer import SpeechRecognizer
from utils.utils import allowed_file, call_video_function, hex_to_rgb

# Create a Flask web application instance
app = Flask(__name__)

# Configure file upload and result folders
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULT_FOLDER'] = 'static/result'
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'avi', 'mov', 'mkv'}

# Ensure the upload and result folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

# Define routes for different web pages/templates

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/speach-recognizer', methods=['GET'])
def speach_html():
    return render_template('speach-recog.html')

@app.route('/image-editor', methods=['GET'])
def image_editor_view():
    return render_template('image-view.html')

# Define a route to get buttons for video editing functions
@app.route("/get_buttons", methods=["GET"])
def get_buttons():
    names = [
        {"name": "Resize Video", "url": 'resize_video', 'input_model': 'resize'},
        {"name": "Add Text To Video", "url": 'add_text_to_video', 'input_model': 'text'},
        {"name": "Flip Video", "url": 'flip_video', 'input_model': 'single'},
        {"name": "Extract Frames", "url": 'extract_frames', 'input_model': 'single'},
        {"name": "Remove Audio", "url": 'remove_audio', 'input_model': 'single'},
        {"name": "Join videos", "url": 'join_videos', 'input_model': 'files'},
    ]
    result = {
        "success": True,
        "names": names,
    }
    return result

# Define a route to get buttons for image editing functions
@app.route("/image-buttons", methods=["GET"])
def image_buttons():
    names = [
        {"name": "Image Blur", "url": 'image_blur'},
        {"name": "Image Contour", "url": 'image_contour'},
        {"name": "Image Detail", "url": 'image_detail'},
        {"name": "Image Edge Enhance", "url": 'image_edge_enhance'},
        {"name": "Image Emboss", "url": 'image_emboss'},
        {"name": "Image Sharpen", "url": 'image_sharpen'},
        {"name": "Image Smooth", "url": 'smooth_filter'},
        {"name": "Resized Image", "url": 'resized_image'},
        {"name": "Black and White", "url": 'black_and_white'},
    ]

    result = {
        "success": True,
        "names": names,
    }
    return result

# Define a route to upload files for video editing
@app.route('/upload', methods=['POST'])
def upload_file():
    success_messages = []
    error_messages = []
    filepath = []
    function_name = request.form.get('function_name')
    colorPickerInput = request.form.get('colorPickerInput')
    video_text = request.form.get('video_text')
    height = request.form.get('height')
    width = request.form.get('width')

    files = request.files.getlist('files')
    for file in files:
        if file and allowed_file(app, file.filename):
            filename = str(int(time.time())) + secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            success_messages.append(f'File "{filename}" uploaded successfully. File path: {file_path}')
            filepath.append(file_path)
        else:
            error_messages.append(f'Invalid file: {file.filename}')
    
    editor = VideoEditor()
    result = call_video_function(editor, function_name, filepath, colorPickerInput, video_text, width, height)

    if success_messages:
        return jsonify({'success': success_messages, 'path': result})
    else:
        return jsonify({'error': 'No valid files uploaded'})

# Define a route to upload images for image editing
@app.route('/upload-image', methods=['POST'])
def upload_image():
    try:
        if 'image' not in request.files:
            return jsonify({'message': 'No file part'}), 400
        file = request.files['image']
        function_name = request.form.get('function_name')
        height = request.form.get('height')
        width = request.form.get('width')
        image_processor = ImageProcessor()
        file = file.read()
        file = image_processor.convert_image(file)
        
        if function_name == "resized_image":
            image = getattr(image_processor, function_name)(file, int(width), int(height))
        else:
            image = getattr(image_processor, function_name)(file)
        file_name = str(int(time.time())) + '.jpg'
        image_processor.save_image(image, file_name)
        return jsonify({'message': 'File uploaded successfully', 'file': file_name})
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

# Define a route to upload audio files for speech recognition
@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    try:
        if 'audio' not in request.files:
            return jsonify({'message': 'No file part'}), 400
        file = request.files['audio']
        audio_to_text = SpeechRecognizer()
        result = audio_to_text.recognize_audio(file)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

# Run the Flask app if this file is the main program
if __name__ == '__main__':
    app.run()
