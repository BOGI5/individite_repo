from . import password_encrypting
from . import password_decrypting
from . import hashing
from . import Test_password

def encrypt(user, password, website, key, json_object):
    return password_encrypting.encrypt_password(user, password, website, key, json_object)


def decrypt(user, website, key, json_object):
    return password_decrypting.decrypt_password(user, website, key, json_object)

def hash_key(key):
    return hashing.hash_key(key)

def check_password(user, website, key, json_object):
    if str(decrypt(user, website, key, json_object)):
        return Test_password.check_password(str(decrypt(user, website, key, json_object)))
    return False

def common_used_passwords(user, website, key, json_object):
    if str(decrypt(user, website, key, json_object)):
        return Test_password.common_used_passwords(str(decrypt(user, website, key, json_object)))
    return False