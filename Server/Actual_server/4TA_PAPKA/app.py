from flask import Flask, render_template, request, redirect
import os
from base64_to_image import get_image
import Password_work
from face_verification import check_image


app = Flask(__name__)

#app.config['UPLOAD_FOLDER'] = r'/media/manol/ESD-USB/hacktues/hacktues/uploads'


@app.route('/')
def home():
    return render_template('homepage.html')



@app.route('/signup/', methods =["GET", "POST"])
def signup():
    if request.method == "POST":
        takendataURL = request.form.get("dataURL")
        username = request.form.get("Name")
        password = request.form.get("Password")
        get_image(takendataURL, username)
        passwords(username, password)

    return render_template('signup.html')


@app.route('/passwords/', methods =["GET", "POST"])
def passwords(username, password):
    if request.method == "POST":
        newwebsite = request.form.get('site_url')
        newpassword = request.form.get('site_url')
        Password_work.encrypt('user', newpassword, newwebsite, check_image(), password, username)


    return render_template('passwords.html')

if __name__ == '__main__':
    app.run()
