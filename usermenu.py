from password_generator import PasswordGenerator
import json
import os

if not os.path.isfile('./users.dic'):
    with open('./users.dic', 'w') as f:
        f.write('{}')

def open_file():
    with open('./users.dic') as db:
        f_dict = db.read()
    return json.loads(f_dict)

def write_file(js_dict):
    dict_json = json.dumps(js_dict)
    with open('./users.dic', 'w') as db:
        db.write(dict_json)
        
def generate_password():
    rng_password = PasswordGenerator()
    rng_password.minlen = 4
    rng_password.maxlen = 8
    rng_password.minnumbers = 1
    rng_password.minschars = 1
    rng_password.minuchars = 1
    return rng_password.generate()


def create_user(*args):
    js_dict = open_file()
    if args[0] in js_dict:
        return False, None
    passwordo = args[1]
    if not args[1]:
        passwordo = generate_password()
    js_dict[args[0]] = passwordo
    write_file(js_dict)
    return True, passwordo


def user_login(*args):
    js_dict = open_file()
    if args[0] in js_dict and js_dict[args[0]] == args[1]:
        return True
    else:
        return False


def delete_user(user_name):
    js_dict = open_file()
    if user_name not in js_dict:
        return False
    else:
        del js_dict[user_name]
    write_file(js_dict)
    return True


def get_list():
    js_dict = open_file()
    return '\n'.join(js_dict.keys())  # users_list
