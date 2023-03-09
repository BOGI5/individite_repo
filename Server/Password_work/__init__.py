from . import password_encrypting
from . import password_decrypting
from . import hashing

def encrypt(user, password, website, key, json_object):
    return password_encrypting.encrypt_password(user, password, website, key, json_object)


def decrypt(user, website, key, json_object):
    return password_decrypting.decrypt_password(user, website, key, json_object)

def hash_key(key):
    return hashing.hash_key(key)