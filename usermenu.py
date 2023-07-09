from password_generator import PasswordGenerator
import argon2
from cryptography.fernet import Fernet
import json
import os
import secret #secret key for Fernet you need to create your own



def hash_pass(password):
    ph = argon2.PasswordHasher()
    hashed_pass = ph.hash(password)
    return hashed_pass


def open_file():
    fernet = Fernet(secret.s_key)
    with open('./users.dic') as encr_db:
        encrypted_dict = encr_db.read()
    decrypted_dict = fernet.decrypt(encrypted_dict)
    return json.loads(decrypted_dict)

def write_file(js_dict):
    dict_json = json.dumps(js_dict)
    with open('./users.dic', 'w') as db:
        db.write(dict_json)
    encrypt_file()

def encrypt_file():
    fernet = Fernet(secret.s_key)
    with open('./users.dic', 'rb') as file:
        original = file.read()

    dict_encrypted = fernet.encrypt(original)

    with open('./users.dic', 'wb') as enc_file:
        enc_file.write(dict_encrypted)

def generate_password():
    rng_password = PasswordGenerator()
    rng_password.minlen = 4
    rng_password.maxlen = 8
    rng_password.minnumbers = 1
    rng_password.minschars = 1
    rng_password.minuchars = 1
    return rng_password.generate()


def create_user(login, password):
    js_dict = open_file()
    if login in js_dict:
        return False, None
    passwordo = password
    if not password:
        passwordo = generate_password()
    js_dict[login] = hash_pass(passwordo)
    write_file(js_dict)
    return True, passwordo


def user_login(login, password):
    js_dict = open_file()
    ph = argon2.PasswordHasher()
    try:
        return ph.verify(js_dict[login], password)
    except (argon2.exceptions.VerifyMismatchError, KeyError):
        return False

def delete_user(user_name):
    js_dict = open_file()
    if user_name not in js_dict:
        return False
    del js_dict[user_name]
    write_file(js_dict)
    return True


def get_list():
    js_dict = open_file()
    return '\n'.join(js_dict.keys())  # users_list

if not os.path.isfile('./users.dic'):
    with open('./users.dic', 'w') as f:
        f.write('{}')
    encrypt_file()