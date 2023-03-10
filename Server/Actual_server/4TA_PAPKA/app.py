from flask import Flask, render_template, request, redirect
import os
from base64_to_image import get_image
import Password_work
from face_verification import check_image
from facial_expression_recognition import face_features
from tensorflow import keras
import json

app = Flask(__name__)

username = ""
password = ""

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/signup/', methods =["GET", "POST"])
def signup():
    if request.method == "POST":
        takendataURL = request.form.get("dataURL")
        global username
        username = str(request.form.get("Name"))
        global password
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


@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.method == "POST":
            takendataURL = request.form.get("dataURL")
            global username
            username = str(request.form.get("Name"))
            global password
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


@app.route('/passwords/', methods=["GET", "POST"])
def passwords():
    if request.method == "POST":
        website = request.form.get("site_url")
        password_to_encrypt = request.form.get("site_pass")
        key = keras.preprocessing.image.load_img(rf'Face_images/{username}.png')
        key = keras.preprocessing.image.img_to_array(key, dtype='float32')
        Password_work.encrypt(username, password_to_encrypt, website, str(key), password, username)
    if request.method == "GET":
        key = keras.preprocessing.image.load_img(rf'Face_images/{username}.png')
        key = keras.preprocessing.image.img_to_array(key, dtype='float32')
        # Go through all the passwords and decrypt them
        with open(rf'Password_work/Database/new_database/{username}.json', 'r') as file:
            json_file = file.read()
            json_file = json.loads(json_file)
            if json_file[username]:
                new_json = json.load({})
                for website in json_file[username]:
                    new_json.update({ "website": website, "password": Password_work.decrypt(username, website, str(key), username, password) })
                return render_template('passwords.html', passwords = json.dumps(new_json))
        

    return render_template('passwords.html')






if __name__ == '__main__':
    app.run()
