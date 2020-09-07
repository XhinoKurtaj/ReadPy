
import os
from flask import Flask, request
from ocr import ocr_core


# define a folder to store and later serve the images
UPLOAD_FOLDER = '/static/uploads'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'jiff'])

app = Flask(__name__)

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and filename.split('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home_page():
    return "Hello World!"

# route and function to handle the upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            data = { 'msg': 'No file selected'}
            return data, 400
        file = request.files['file']
        if  file.filename == '':
            data = { 'msg': 'No file selected'}
            return data, 400
        
        
        if file and allowed_file(file.filename):
            extracted_text = ocr_core(file)
            data = {
                 'msg': 'Successfully processed',
                 'content': extracted_text
                 }
            return data, 200
        
if __name__ == '__main__':
    app.run()