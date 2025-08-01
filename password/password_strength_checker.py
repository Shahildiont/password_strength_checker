import re
import tkinter as tk

def check_password_strength():
    password = entry1.get()  # Get input from Entry widget
    if len(password) < 8:
        result_lab.config(text="Weak : Password is too short (min 8 characters).")
    elif not re.search("[a-z]", password):
        result_lab.config(text="Weak : Missing lowercase letter.")
    elif not re.search("[A-Z]", password):
        result_lab.config(text="Weak : Missing uppercase letter.")
    elif not re.search("[0-9]", password):
        result_lab.config(text="Weak : Missing number.")
    elif not re.search("[!@#$%^&*()_+\-=\[\]{}|;:,.<>/?]", password):
        result_lab.config(text="Weak : Missing special character.")
    else:
        result_lab.config(text="Strong : Password meets requirements.")


def toggle_password():
    if show_password_var.get():
        entry1.config(show="")
    else:
        entry1.config(show="*")

#window
passw=tk.Tk()
passw.title("PASSWORD STRENGTH CHECKER")
passw.geometry("400x300")

#label
tk.Label(passw, text="ENTER YOUR PASSWORD").pack(pady=10)
entry1 = tk.Entry(passw, show="*")
entry1.pack()


show_password_var = tk.BooleanVar()
tk.Checkbutton(passw, text="Show Password", variable=show_password_var, command=toggle_password).pack()

#button
tk.Button(passw, text="CHECK" ,command=check_password_strength).pack(pady=10)

#result
result_lab= tk.Label(passw, text="Result:")
result_lab.pack(pady=10)

#mainloop
passw.mainloop()