from flask import Flask, request, render_template, redirect, url_for
import os
from resume_scanner.scanner import process_resume

app = Flask(__name__)

# Directory for uploaded resumes
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'pdf', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB size limit

# Checks if file extension is docx or pdf
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Uploads Files and scans it for matching side hustle
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Checks if file was properly uploaded
        if 'file' not in request.files:
            return "No file part in the request."
        
        file = request.files['file']

        if file.filename == '':
            return "No file selected for uploading."
        
        # After correct file upload
        if file and allowed_file(file.filename):
            # Saves file to upload folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Processes resume and stores side hustle with highest score in 'highest_hustle' variable
            highest_hustle = process_resume(file_path)

            # Goes to Web Developer Page
            return redirect(url_for('web_developer'))

    return render_template('upload.html')

# Database route
@app.route('/database')
def database():
    return render_template('database.html')

# Web Developer route
@app.route('/web_developer')
def web_developer():
    return render_template('side_hustle_listings/web_developer.html')

# Scriptwriter route
@app.route('/scriptwriter')
def scriptwriter():
    return render_template('side_hustle_listings/scriptwriter.html')

@app.route('/prompt_engineer')
def prompt_engineer():
    return render_template('side_hustle_listings/prompt_engineer.html')


if __name__ == "__main__":
    app.run(debug=True)
