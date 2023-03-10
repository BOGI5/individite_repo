from flask import Flask, render_template, request, redirect
import os
from base64_to_image import get_image


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = r'/media/manol/ESD-USB/hacktues/hacktues/uploads'


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        takendataURL = request.form.get("dataURL")
        username = request.form.get("Name")
        get_image(takendataURL, username)

    return render_template('signup.html')

@app.route('/passwords/')
def passwords():
    #if request.method == "POST":
       # newwebsite = request.form.get("site_url")
       # newpass = request.form.get("site_pass")
        #print(newwebsite + newpass)
    return render_template('passwords.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()