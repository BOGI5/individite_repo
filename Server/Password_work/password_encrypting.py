from cryptography.fernet import Fernet
import os
import hashing
import json


def get_key(key):
    return hashing.hash_key(key)


def save_to_file(user, password, website):
    file = open("database.json", "r")
    if os.path.getsize("database.json") > 0:
        data = file.read()
        data = json.loads(data)
        if (user in data):
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
    file = open("database.json", "w")
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


#encrypt_password("usr", "passd", "wete", "key")