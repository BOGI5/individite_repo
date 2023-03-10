from flask import Flask, render_template, request, redirect
import os
from base64_to_image import get_image


app = Flask(__name__)

#app.config['UPLOAD_FOLDER'] = r'/media/manol/ESD-USB/hacktues/hacktues/uploads'




@app.route('/signup/', methods =["GET", "POST"])
def signup():
    if request.method == "POST":
        takendataURL = request.form.get("dataURL")
        username = request.form.get("Name")

        print(takendataURL)
        print(username)
        get_image(takendataURL, username)

    return render_template('signup.html')




if __name__ == '__main__':
    app.run()