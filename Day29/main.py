import email
from tkinter import *
from tkinter import messagebox
from password_generator import Password_Generator
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

password_generator = Password_Generator()

def generate_password():
    password = password_generator.generate()
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_to_file(data):
    try:
        with open("data.json", "r") as file:
            old_data = json.load(file)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        old_data.update(data)
        with open("data.json", "w") as file:
            json.dump(old_data, file, indent=4)

def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    data = {
        website: {
            "email": email_username,
            "password": password
        }
    }
    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(title="Ooops", message="Please don't leave any fields empty!")
    else:
        write_to_file(data)
        clear_entries()

def clear_entries():
    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            website_data = data[website]
    except KeyError or FileNotFoundError:
        messagebox.showerror(title="Ooops", message="No Data File Found")
    else:
        email = website_data["email"]
        password = website_data["password"]
        messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:").grid(row=1, column=0)
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
website_search = Button(text="Search", command=find_password, width=12).grid(row=1, column=2)

email_username_label = Label(text="Email/Username:").grid(row=2, column=0)
email_username_entry = Entry(width=38)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "jay_issuree@hotmail.co.uk")

password_label = Label(text="Password:").grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()