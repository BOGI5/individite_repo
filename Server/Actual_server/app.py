from flask import Flask, render_template, request, redirect
import os
from base64_to_image import get_image


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = r'/media/manol/ESD-USB/hacktues/hacktues/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the file from the POST request
    file = request.files['photo']
    # Save the file to the specified folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect('/upload')

@app.route('/upload', methods=['GET'])
def show_upload_form():
    return render_template('upload.html')

@app.route('/temp', methods=['GET', 'POST'])
def temp():
    if request.method == "POST":
        takendataURL = request.form.get("dataURL")
        username = request.form.get("Name")
        path = rf'/home/bogi5/Github/individite_repo/Server/Face_image_base64/{username}.txt'

        with open(path, 'w') as file:
            file.write(takendataURL)
        get_image()

    return render_template('temp.html')

@app.route('/bg/')
def bgindex():
    return render_template('bg-index.html')

@app.route('/bg/upload', methods=['POST'])
def bgupload():
    # Get the file from the POST request
    file = request.files['file']
    # Save the file to the specified folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return 'File uploaded successfully!'



@app.route('/bg/upload', methods=['GET'])
def bgshow_upload_form():
    return render_template('bg-upload.html')

@app.route('/bg/temp')
def bgidk():
    return render_template('bg-idk.html')

if __name__ == '__main__':
    app.run()