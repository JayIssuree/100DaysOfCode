from tkinter import *
from tkinter import messagebox
from password_generator import Password_Generator
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

password_generator = Password_Generator()

def generate_password():
    password = password_generator.generate()
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_to_file(data):
    with open("data.txt", "a") as file:
        file.write(data)

def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    data = f"{website} | {email_username} | {password} \n"

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(title="Ooops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email_username} \n Password: {password} \n Is it ok to save?")
        if is_ok:
            write_to_file(data)
            clear_entries()

def clear_entries():
    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:").grid(row=1, column=0)
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

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