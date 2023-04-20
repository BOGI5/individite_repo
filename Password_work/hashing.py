import hashlib
import base64

def hash_key(key):
    key = hashlib.sha256(key.encode()).hexdigest()
    key = bytes.fromhex(key)
    key = base64.b64encode(key).decode()
    return key