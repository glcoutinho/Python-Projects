import tkinter
from tkinter import *
from tkinter import messagebox
import random
import json


# ______________________________BUTTON_________________________________#
def find_password():
    web_get = Website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)  # opens and reads

    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message=f"No Data file found")

    else:
        if web_get in data:
            email = data[web_get]["email"]
            password = data[web_get]["password"]
            messagebox.showinfo(title="User details", message=f"Websites email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="ERROR", message=f"No details for the website exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def Password_Generator_Project():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_letter + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)  # join
    Password_entry.insert(0, password)
    pyperclip.copy(password)
    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    web_get = Website_entry.get()
    email_get = Email_entry.get()
    pass_get = Password_entry.get()

    new_data = {
        web_get: {
            "email": email_get,
            "password": pass_get
        }
    }

    if len(web_get) == 0 or len(email_get) == 0 or len(pass_get) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # opens and reads
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)  # update with new dictionary

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            Website_entry.delete(0, "end")
            Password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)  # x and y position
canvas.grid(row=0, column=1)

Website_Label = tkinter.Label(text="Website: ")
Website_Label.grid(row=1, column=0)
Website_entry = Entry(width=28)
Website_entry.focus()
Website_entry.get()
Website_entry.grid(column=1, row=1)

Email_Label = tkinter.Label(text="Email/Username: ")
Email_Label.grid(column=0, row=2)
Email_entry = Entry(width=45)
Email_entry.insert(0, "example@gmail.com")
Email_entry.get()
Email_entry.grid(column=1, row=2, columnspan=2)

Password_Label = tkinter.Label(text="Password: ")
Password_Label.grid(column=0, row=3)
Password_entry = Entry(width=25)
Password_entry.grid(column=1, row=3)
Password_button = Button(text="Generate Password", command=Password_Generator_Project)
Password_button.grid(column=2, row=3)

button_add = Button(text="Add", width=32, command=save_pass)
button_add.grid(column=1, row=4, columnspan=2)

Search_button = Button(text="Search", width=10, command=find_password)
Search_button.grid(column=2, row=1)

window.mainloop()
