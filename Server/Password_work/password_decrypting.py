from cryptography.fernet import Fernet
from . import hashing
import os
import json


def get_key(key):
    return hashing.hash_key(key)


def read_from_file(user, website):
    # get the path to the file
    path = os.path.dirname(os.path.abspath(__file__))
    path += r"/database.json"
    file = open(path, "r")
    if os.path.getsize(path) > 0:
        data = file.read()
        data = json.loads(data)
        if (user in data):
            if(website in data[user]):
                password = data[user][website]["password"]
                file.close()
                return password
            else:
                file.close()
                return False
        else:
            file.close()
            return False
    else:
        file.close()
        return False
    

def decrypt_password(user, website, key):
    key = get_key(key)
    password = read_from_file(user, website)
    if password:
        password = password.encode()
        password = Fernet(key).decrypt(password)
        return password.decode()
    else:
        return False



if __name__ == "__main__":
    print(decrypt_password("usr", "wete", "key"))
