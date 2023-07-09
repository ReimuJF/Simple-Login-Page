from usermenu import *
import tkinter as tk
import tkinter.messagebox


def login_button():
    check = user_login(entry_login.get(), entry_password.get())
    if check:
        tkinter.messagebox.showinfo("Success", f"Hello {entry_login.get()}")
        clear_entry()
    else:
        tkinter.messagebox.showinfo("Error", "Wrong login or password")


def sign_button():
    check, check_pass = create_user(entry_login.get(), entry_password.get())
    if check:
        tkinter.messagebox.showinfo("Success", f"User {entry_login.get()} created")
        tkinter.messagebox.showinfo("Success", f"your pass: {check_pass}" if
        check_pass != entry_password.get() else "Remember your password")
        clear_entry()
    else:
        tkinter.messagebox.showinfo("Error", "This name already taken")


def get_button():
    users_list = get_list()
    tkinter.messagebox.showinfo("Success", f"{users_list}")


def delete_button():
    check = delete_user(entry_login.get())
    if check:
        tkinter.messagebox.showinfo("Success", f"User was deleted")
        clear_entry()
    else:
        tkinter.messagebox.showinfo("Error", "User not found")


def clear_entry():
    entry_login.delete(0, tk.END)
    entry_password.delete(0, tk.END)

if __name__ == "__main__":
    window = tk.Tk()
    window.title('Simple Login Page')
    window.resizable(width=False, height=False)

    entry_login = tk.Entry(width=25)
    entry_password = tk.Entry(width=25, show="*")
    entry_login.grid(row=0, column=0, padx=10)
    entry_password.grid(row=1, column=0, padx=10)
    button_login = tk.Button(text='LOGIN', width=15, command=login_button)
    button_login.grid(row=0, column=1, padx=10, pady=5)
    button_sign = tk.Button(text='SIGN UP', width=15, command=sign_button)
    button_sign.grid(row=1, column=1, padx=10)
    button_get = tk.Button(text='GET USER LIST', width=15, command=get_button)
    button_get.grid(row=2, column=0, pady=10, sticky='ws', padx=5)
    button_delete = tk.Button(text='DELETE USER', width=15, command=delete_button)
    button_delete.grid(row=2, column=1, pady=10, sticky='es', padx=10)
    window.mainloop()