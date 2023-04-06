from flask import Flask, render_template, request, redirect, session
import os
from base64_to_image import get_image
import Password_work
from face_verification import check_image
from facial_expression_recognition import face_features
from tensorflow import keras
import json
from flask_session import Session
from datetime import timedelta

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.before_first_request
def make_session_timeout():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/signup/', methods =["GET", "POST"])
def signup():
    if request.method == "POST":
        takendataURL = request.form.get("dataURL")
        username = str(request.form.get("Name"))
        password = str(request.form.get("Password"))
        path_for_image = os.path.dirname(os.path.abspath(__file__))
        path_for_image += r'/Face_images/' + username + '.png'
        if os.path.exists(path_for_image):
            return render_template('signup.html', message = "This username is already taken")
        session["username"] = username
        session["password"] = password
        get_image(takendataURL, username, r"/Face_images/")
        key = keras.preprocessing.image.load_img(path_for_image)
        key = keras.preprocessing.image.img_to_array(key, dtype='float32')
        Password_work.encrypt('dtfyuhgfcyhugfdxgyhty678yutre567uyhgtfrde456ytfdre54678iuygtfr56t78uijhgty67890poi8967tyuio876rtfghuio87y6t5rtyui8y76t54ertfyguhy76t54e3erdfghjui7y6t54eerdfghui87654ertfghui8y7654ersdfghjui876rtyghio98765rtyui87y6t5ertyuio8uy76t5rrefghuio8u7y', 'test', 'test', str(key), password, username)
        return redirect("/passwords/")

    return render_template('signup.html')


@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        takendataURL = request.form.get("dataURL")
        username = str(request.form.get("Name"))
        password = str(request.form.get("Password"))
        get_image(takendataURL, username, r'/Verify_face/')
        get_image(takendataURL, username, r'/Face_expressions/')
        path_for_image = os.path.dirname(os.path.abspath(__file__))
        path_for_image += r'/Face_images/' + username + '.png'
        if not os.path.exists(path_for_image):
            return render_template('login.html', data = "User does not exist")
        key = check_image(username)
        if key != False:
            if Password_work.decrypt('dtfyuhgfcyhugfdxgyhty678yutre567uyhgtfrde456ytfdre54678iuygtfr56t78uijhgty67890poi8967tyuio876rtfghuio87y6t5rtyui8y76t54ertfyguhy76t54e3erdfghjui7y6t54eerdfghui87654ertfghui8y7654ersdfghjui876rtyghio98765rtyui87y6t5ertyuio8uy76t5rrefghuio8u7y', 'test', key, username, password) != "Blob":
                if face_features(username, 'happy'):
                    session["tempusername"] = username
                    session["temppassword"] = password
                    print(redirect("/login2/"))
                    return redirect("/login2/")
                else:
                    #print(face_features(username))
                    print('HELOOOOOOOOOOOOOOO')
                    return render_template('login.html', data = "Please smile")
            else:
                print('password')
                return render_template('login.html', data = "Wrong password")
        else:
            print('face')
            return render_template('login.html', data = "Face not recognized")

    return render_template('login.html', data = "")


@app.route('/passwords/', methods=["GET", "POST"])
def passwords():
    if not session.get("username"):
        return redirect("/")
    username = session.get("username")
    password = session.get("password")
    if request.method == "POST":
        website = request.form.get("site_url")
        password_to_encrypt = request.form.get("site_pass")
        path_for_image = os.path.dirname(os.path.abspath(__file__))
        path_for_image += r'/Face_images/' + username + '.png'
        key = keras.preprocessing.image.load_img(path_for_image)
        key = keras.preprocessing.image.img_to_array(key, dtype='float32')
        Password_work.encrypt(username, password_to_encrypt, website, str(key), password, username)
    if request.method == "GET":
        path_for_image_and_database = os.path.dirname(os.path.abspath(__file__))
        path_for_image_and_database += r'/Face_images/' + username + '.png'
        key = keras.preprocessing.image.load_img(path_for_image_and_database)
        key = keras.preprocessing.image.img_to_array(key, dtype='float32')
        # Go through all the passwords and decrypt them
        path_for_image_and_database = os.path.dirname(os.path.abspath(__file__))
        path_for_image_and_database += r'/Password_work/Database/new_database/' + username + '.json'
        with open(path_for_image_and_database, 'r') as file:
            json_file = file.read()
            json_file = json.loads(json_file)
            try:
                json_file[username]
            except KeyError:
                return render_template('passwords.html')
            new_json = list()
            for website in json_file[username]:
                new_json.append( { "website": website, "password": Password_work.decrypt(username, website, str(key), username, password) } )
            new_json = json.dumps(new_json)

            generated_password = str(Password_work.GP(16))
        return render_template('passwords.html', data2 = generated_password, data = new_json)
        

    return redirect("/passwords/")

@app.route('/delete/', methods=["GET", "POST"])
def delete():
    if not session.get("username"):
        return redirect("/")
    if request.method == "GET":
        website = request.args.get('del')
        username = session.get("username")
        if website:
            Password_work.delete_password(username, website, username)
    return redirect("/passwords/")


@app.route('/logout/')
def logout():
    if not session.get("username"):
        return redirect("/")
    session.clear()
    return redirect("/")

@app.route('/login2/', methods=["GET", "POST"])
def login2():
    if request.method == "POST":
        takendataURL = request.form.get("dataURL")
        username = session.get("tempusername")
        password = session.get("temppassword")
        get_image(takendataURL, username, r'/Verify_face/')
        get_image(takendataURL, username, r'/Face_expressions/')
        key = check_image(username)
        if key != False:
            if face_features(username, 'surprise'):
                print('HELOOOOOO')
                session["username"] = username
                session["password"] = password
                return redirect("/passwords/")
            else:
                #print(face_features(username))
                return render_template('login2.html', data = "Please make a surprised face")
        else:
            print('face')
            return render_template('login2.html', data = "Face not recognized")
    print('dyyyyyyyy')
    return render_template('login2.html', data = "")


if __name__ == '__main__':
    app.run()
