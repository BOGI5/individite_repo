from cryptography.fernet import Fernet
import os
import hashing
import json


def get_key(key):
    return hashing.hash_key(key)


def save_to_file(user, password, website):
    file = open("example_database.json", "r")
    if os.path.getsize("example_database.json") > 0:
        data = file.read()
        data = json.loads(data)
        if (user in data):
            if(website in data[user]):
                data[user][website]["password"] = password
            else:
                #add new website
                print("not done")
        else:
            #add new user
            print("not done")
            
    else:
        data = '{"${user}": {"${website}":{ "password": "${password}"}}}'

    file.close()
    #file = open("database.json", "w")
    #file.write(json.dumps(data))
    #file.close()



def encrypt_password(user, password, website, key):
    key = get_key(key)
    password = password.encode()
    user = user.encode()
    website = website.encode()
    password = Fernet(key).encrypt(password)
    save_to_file(user, password, website)
    return True


encrypt_password("user", "password", "website", "key")