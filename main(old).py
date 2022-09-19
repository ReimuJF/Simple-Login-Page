from password_generator import PasswordGenerator
import json
from getpass import getpass
import os

if not os.path.isfile('./users.dic'):
    with open('./users.dic', 'w') as f:
        f.write('{}')


def create_user():
    os.system('cls')
    with open('./users.dic') as db:
        f_dict = db.read()
    js_dict = json.loads(f_dict)
    new_id = input('Enter your id: ')
    while new_id in js_dict:
        new_id = input('Enter your id: ')
        if new_id in js_dict:
            print("Users exist. Try another id")
    passwordo = getpass("Enter password, just Enter for random generated ")
    if not passwordo:
        rng_password = PasswordGenerator()
        rng_password.minlen = 4
        rng_password.maxlen = 8
        rng_password.minnumbers = 1
        rng_password.minschars = 1
        rng_password.minuchars = 1
        passwordo = rng_password.generate()
        print(f'your randomly generated password is {passwordo}')
    js_dict[new_id] = passwordo
    dict_json = json.dumps(js_dict)
    db = open('./users.dic', 'w')
    db.write(dict_json)
    db.close()
    input()


def user_login():
    os.system('cls')
    with open('./users.dic') as db:
        f_dict = db.read()
    js_dict = json.loads(f_dict)
    for _ in range(5):
        login, pas = input('Enter login: '), getpass('Enter password: ')
        if login in js_dict and js_dict[login] == pas:
            print(f'Hello {login}')
            break
        else:
            print('Wrong login or password')
        input()
    else:
        input('You out of attempt get back later')
        return False
    input()


def delete_user():
    os.system('cls')
    with open('./users.dic') as db:
        f_dict = db.read()
    js_dict = json.loads(f_dict)
    u_id = input('Enter user id ')
    if u_id not in js_dict:
        input("User not found")
        return False
    else:
        del js_dict[u_id]
        input('user deleted ')
    dict_json = json.dumps(js_dict)
    db = open('./users.dic', 'w')
    db.write(dict_json)
    db.close()
    input()


def get_list():
    os.system('cls')
    with open('./users.dic') as db:
        f_dict = db.read()
    js_dict = json.loads(f_dict)
    print(*js_dict.keys(), sep=',', end='.')
    input()


def menu():
    actions = {'login': user_login, 'sign': create_user, 'delete': delete_user,
               'get': get_list, 'exit': exit}
    while True:
        os.system('cls')
        print('Welcome to test program:')
        print(*actions, sep='\n', end='\n')
        welcome = input('Enter your command: ')
        if welcome in actions:
            actions[welcome]()
        else:
            print('wut?')


if __name__ == '__main__':
    menu()