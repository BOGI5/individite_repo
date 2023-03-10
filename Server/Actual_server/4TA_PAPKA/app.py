from flask import Flask, render_template, request, redirect
import os
from base64_to_image import get_image
import Password_work
from face_verification import check_image
from facial_expression_recognition import face_features
from tensorflow import keras

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/signup/', methods =["GET", "POST"])
def signup():
    if request.method == "POST":
        takendataURL = request.form.get("dataURL")
        username = str(request.form.get("Name"))
        password = str(request.form.get("Password"))
        get_image(takendataURL, username, r"/Face_images/")
        with open(r'Verify_face/name.txt', 'w') as file:
            file.write(username)
        key = keras.preprocessing.image.load_img(rf'Face_images/{username}.png')
        key = keras.preprocessing.image.img_to_array(key, dtype='float32')
        get_image(takendataURL, username, r"/Verify_face/")
        Password_work.encrypt('test', 'test', 'test', str(key), password, username)
        os.remove(r'Verify_face/name.txt')
        os.remove(rf'Verify_face/{username}.png')

    return render_template('signup.html')

'''
@app.route('/passwords/', methods=["GET", "POST"])
def passwords(username, password):
    if request.method == "POST":
        if request.method == "POST":
            takendataURL = request.form.get("dataURL")
            username = request.form.get("Name")
            password = request.form.get("Password")
            with open(r'Verify_face/name.txt', 'w') as file:
                file.write(username)
            get_image(takendataURL, username, r"/Verify_face/")
            if check_image():
                print(1)
            #Password_work.decrypt('test', 'test', 'test', str(key), password, username)

    return render_template('passwords.html')
'''


@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.method == "POST":
            takendataURL = request.form.get("dataURL")
            username = str(request.form.get("Name"))
            password = str(request.form.get("Password"))
            get_image(takendataURL, username, r"/Verify_face/")
            get_image(takendataURL, username, r"/Face_expressions/")
            key = str(check_image())
            check = False
            if key:
                if Password_work.decrypt('test', 'test', key, username, password):
                    if face_features() == 'happy':
                        check = True
            print(check)

    return render_template('login.html')


if __name__ == '__main__':
    app.run()
