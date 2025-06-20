from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Set the upload folder using absolute path
UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Mock user data for login
USER_DATA = {
    "username": "admin",
    "password": "password"
}

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == USER_DATA['username'] and password == USER_DATA['password']:
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid username or password"}), 401

# File upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"success": False, "message": "No selected file"}), 400

    # Save the file to the upload folder
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    return jsonify({"success": True, "message": "File uploaded successfully", "file_path": file_path})

# Serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route to list all files
@app.route('/files', methods=['GET'])
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return jsonify({"files": files})

# Delete file route
@app.route('/delete', methods=['POST'])
def delete_file():
    data = request.get_json()
    filename = data.get('filename')

    if not filename:
        return jsonify({"success": False, "message": "Filename is required"}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if not os.path.exists(file_path):
        return jsonify({"success": False, "message": "File not found"}), 404

    try:
        os.remove(file_path)
        return jsonify({"success": True, "message": "File deleted successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Failed to delete file: {str(e)}"}), 500

# Save edited file route
@app.route('/save', methods=['POST'])
def save_file():
    data = request.get_json()
    filename = data.get('filename')
    content = data.get('content')

    if not filename or content is None:
        return jsonify({"success": False, "message": "Filename and content are required"}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return jsonify({"success": True, "message": "File saved successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Failed to save file: {str(e)}"}), 500

# Create folder route
@app.route('/create-folder', methods=['POST'])
def create_folder():
    data = request.get_json()
    folder_name = data.get('folderName')

    if not folder_name:
        return jsonify({"success": False, "message": "Folder name is required"}), 400

    folder_path = os.path.join(app.config['UPLOAD_FOLDER'], folder_name)

    if os.path.exists(folder_path):
        return jsonify({"success": False, "message": "Folder already exists"}), 400

    try:
        os.makedirs(folder_path)
        return jsonify({"success": True, "message": "Folder created successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": f"Failed to create folder: {str(e)}"}), 500

# Serve static files (CSS, JS, etc.)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# Default route to serve the HTML file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)