from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symb in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    pyperclip.copy(password)
    password_entry.insert(0, f"{password}")


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("password_list.json", "r") as passwords:
            data_1 = json.load(passwords)
    except FileNotFoundError:
        messagebox.showinfo(title=website, message="No Data File Found")
    else:
        if website in data_1:
            info = ""
            for key in data_1[website]:
                info += f"{key}: {data_1[website][key]}\n"
            messagebox.showinfo(title=website, message=info + "\npassword copied.")
            pyperclip.copy(data_1[website]["password"])
        else:
            messagebox.showinfo(title=website, message="No details for the website exists")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def write():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    data = {
        website: {"email": email,
                  "password": password
                  }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any box empty")
        return
    else:
        try:
            with open("password_list.json", "r") as passwords:
                dat = json.load(passwords)
        except FileNotFoundError:
            with open("password_list.json", "w") as passwords:
                json.dump(data, passwords, indent=4)
        else:
            with open("password_list.json", "w") as passwords:
                dat.update(data)
                json.dump(dat, passwords, indent=4)
                print(dat)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password's")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
myimg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=myimg)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=22)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "lsanchez5403@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

search = Button(text="Search", width=15, command=find_password)
search.grid(row=1, column=2)
generate = Button(text="Generate Password", command=generate_pass)
generate.grid(row=3, column=2, columnspan=1)

add = Button(text="Add", width=34, command=write)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
