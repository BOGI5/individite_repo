from cryptography.fernet import Fernet
import os
from . import hashing
import json


def get_key(key):
    return hashing.hash_key(key)


def save_to_file(user, password, website):
    # get the path to the file
    path = os.path.dirname(os.path.abspath(__file__))
    path += r"/database.json"
    file = open(path, "r")
    # checks if file is empty
    if os.path.getsize(path) > 0:
        data = file.read()
        data = json.loads(data)
        # checks if user is in file
        if (user in data):
            # checks if website is in file
            if(website in data[user]):
                del data[user][website]["password"]
                new_data = {"password": str(password)}
                data[user][website].update(new_data)
            else:
                new_data = {str(website):{"password": str(password)}}
                data[user].update(new_data)
        else:
            new_data = {str(user): {str(website):{ "password": str(password)}}}
            data.update(new_data)
            
    else:
        data = {str(user): {str(website):{ "password": str(password)}}}

    file.close()
    file = open(path, "w")
    file.write(json.dumps(data))
    file.close()



def encrypt_password(user, password, website, key):
    key = get_key(key)
    password = password.encode()
    user = user.encode().decode()
    website = website.encode().decode()
    password = Fernet(key).encrypt(password)
    save_to_file(user, password.decode(), website)
    return True



if __name__ == "__main__":
    encrypt_password("usr", "passd", "wete", "key")