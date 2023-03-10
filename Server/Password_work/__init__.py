from . import password_encrypting
from . import password_decrypting
from . import hashing
from . import Test_password
# from . import password_generator


def encrypt(user, password, website, key, password_verify, username):
    return password_encrypting.encrypt_password(user, password, website, key, password_verify, username)


def decrypt(user, website, key, username, password_verify):
    return password_decrypting.decrypt_password(user, website, key, username, password_verify)

def hash_key(key):
    return hashing.hash_key(key)

def check_password(user, website, key, username, password_verify):
    if decrypt(user, website, key, username, password_verify):
        return Test_password.check_password(str(decrypt(user, website, key, username, password_verify)))
    return False

def common_used_passwords(user, website, key, username, password_verify):
    if decrypt(user, website, key, username, password_verify):
        return Test_password.common_used_passwords(str(decrypt(user, website, key, username, password_verify)))
    return False

# def generate_password(len, key_word=""):
#     return password_generator.generate_password(len, key_word)