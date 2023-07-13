from password_generator import PasswordGenerator
import argon2
from cryptography.fernet import Fernet
import json
import os
import secret #secret key for Fernet you need to create your own


class Login:
    def __init__(self):
        self.ph = argon2.PasswordHasher()
        self.fernet = Fernet(secret.s_key)
        self.dbfile = './users.dic'
        if not os.path.isfile(self.dbfile):
            with open(self.dbfile, 'w') as f:
                f.write('{}')
            self.encrypt_file()
    def hash_pass(self,password):
        hashed_pass = self.ph.hash(password)
        return hashed_pass

    def open_file(self):
        with open(self.dbfile) as encr_db:
            encrypted_dict = encr_db.read()
        decrypted_dict = self.fernet.decrypt(encrypted_dict)
        return json.loads(decrypted_dict)

    def write_file(self, js_dict):
        dict_json = json.dumps(js_dict)
        with open(self.dbfile, 'w') as db:
            db.write(dict_json)
        self.encrypt_file()

    def encrypt_file(self):
        with open(self.dbfile, 'rb') as file:
            original = file.read()

        dict_encrypted = self.fernet.encrypt(original)

        with open(self.dbfile, 'wb') as enc_file:
            enc_file.write(dict_encrypted)

    @staticmethod
    def generate_password():
        rng_password = PasswordGenerator()
        rng_password.minlen = 4
        rng_password.maxlen = 8
        rng_password.minnumbers = 1
        rng_password.minschars = 1
        rng_password.minuchars = 1
        return rng_password.generate()


    def create_user(self, login, password):
        js_dict = self.open_file()
        if login in js_dict:
            return False, None
        passwordo = password
        if not password:
            passwordo = self.generate_password()
        js_dict[login] = self.hash_pass(passwordo)
        self.write_file(js_dict)
        return True, passwordo


    def user_login(self, login, password):
        js_dict = self.open_file()
        ph = argon2.PasswordHasher()
        try:
            return ph.verify(js_dict[login], password)
        except (argon2.exceptions.VerifyMismatchError, KeyError):
            return False

    def delete_user(self, user_name):
        js_dict = self.open_file()
        if user_name not in js_dict:
            return False
        del js_dict[user_name]
        self.write_file(js_dict)
        return True


    def get_list(self):
        js_dict = self.open_file()
        return '\n'.join(js_dict) if len(js_dict) > 0 else 'No users found' # users_list