import json
import random
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_input.get()

    email = email_input.get()
    password = password_input.get()

    new_dict = {
        website: {
            'email': email,
            'password': password,
        }
    }
    if website == '' or password == '' or email == '':
        messagebox.showerror(title='Field are empty', message="Don't leave any of the fields empty")
    else:
        try:
            # 1. Reading old data
            with open("data.json", mode='r') as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", mode='w') as file:
                json.dump(new_dict, file, indent=4)

        else:
            data.update(new_dict)
            with open("data.json", mode='w') as file:
                json.dump(data, file, indent=4)

        website_input.delete(0, END)
        website_input.focus()
        password_input.delete(0, END)


# ---------------------------- Search Password ------------------------------- #

def search_password():
    website = website_input.get()
    if website == '':
        messagebox.showwarning(title='Field is empty', message="Enter the name of the website")
    else:

        try:
            with open("data.json", mode='r') as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title='No data', message='No data file found!')
        else:
            # if website in data:
            #     email = data[website]["email"]
            #     password = data[website]["password"]
            #     messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            # else:
            #     messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

            try:
                search_result = data[website]
            except KeyError:
                messagebox.showerror(title='Website does not exist',
                                     message='The website you are looking for does not exists!')
            else:
                pyperclip.copy(search_result['password'])
                messagebox.showinfo(title="Password Details",
                                    message=f"Website: {website}\nEmail: {search_result['email']}\n"
                                            f"Password: {search_result['password']}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
my_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=my_img, anchor=CENTER)
canvas.grid(row=0, column=1)

# website label

website_label = Label(text='Website:')
website_input = Entry(width=25)
website_input.focus()
website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1, columnspan=2)

search_button = Button(text='Search', command=search_password)
search_button.grid(row=1, column=2)

email_label = Label(text='Email/Username:')
email_input = Entry(width=25)
email_input.insert(0, 'sujalgupta6100@gmail.com')
email_label.grid(row=2, column=0)
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password:')
password_input = Entry(width=25)
password_label.grid(row=3, column=0)
password_input.grid(row=3, column=1, columnspan=2)

generate_button = Button(text='Generate', command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
