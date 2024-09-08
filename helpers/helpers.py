import hashlib
import os


def enc_input(input:str):
    if not input:
        raise Exception("No Input To Process!!")
    salt = os.urandom(32)
    hashed = hashlib.pbkdf2_hmac('sha-256',input.encode('utf-8'), salt, 100000)
    hashed = (salt+hashed).hex()
    return hashed
