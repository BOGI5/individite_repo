from password_encrypting import encrypt_password
from password_decrypting import decrypt_password
from hashing import hash_key

def hash(text):
    return hash_key(text)

def encrypt(user, password, website, key):
    return encrypt_password(user, password, website, key)

def decrypt(user, website, key):
    return decrypt_password(user, website, key)
