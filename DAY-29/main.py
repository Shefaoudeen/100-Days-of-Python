from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for char in range(nr_letters)]

    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_details():

    website = web_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website:{
        "email":email,
        "password":password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message=f"Please don't leave any fields empty!")

    else:
        try:
            with open("data.json","r") as data_file:
                try:
                    data = json.load(data_file)
                    data.update(new_data)
                except:
                    data = {}
                    data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                data = {}
                data.update(new_data)
        finally:
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
                web_input.delete(0,END)
                password_input.delete(0, END)

# ---------------------------- Search ------------------------------- #

def search_password():
    try:
        with open("data.json",'r') as data_file:
            website = web_input.get()

            if len(website) == 0:
                messagebox.showinfo(title=f"NOTE", message=f"Please Enter a website name")

            else:
                data_Set = json.load(data_file)

                try:
                    required_data = data_Set[website]
                    email = required_data["email"]
                    password = required_data["password"]
                    messagebox.showinfo(title=f"{website}", message=f"Email : {email}\nPassword : {password}")
                except KeyError:
                    messagebox.showinfo(title=f"NO DATA", message=f"DATA NOT FOUND")
                finally:
                    web_input.delete(0,END)
    except FileNotFoundError:
        messagebox.showinfo(title=f"NO DATA", message=f"DATA NOT FOUND")
# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Password Manager")
window.minsize(width=200,height=200)
window.config(pady=20,padx=20,bg="white")

canvas = Canvas(width=200,height=200,bg="white",highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

#texts

web_text = Label()
web_text.config(text='Website: ',font=('Arial',10),bg='white')
web_text.grid(row=1,column=0)

email_text = Label()
email_text.config(text='Email/Username: ',font=('Arial',10),bg='white')
email_text.grid(row=2,column=0)

password_text = Label()
password_text.config(text='Password: ',font=('Arial',10),bg='white')
password_text.grid(row=3,column=0)

#inputs

web_input = Entry()
web_input.config(width=35)
web_input.focus()
web_input.grid(row=1,column=1,columnspan=2)

email_input = Entry()
email_input.config(width=35,justify='left')
email_input.insert(0,"shefaoudeen123@gmail.com")
email_input.grid(row=2,column=1,columnspan=2)

password_input = Entry()
password_input.config(width=21,justify='left')
password_input.grid(row=3,column=1)

#buttons

search_btn = Button()
search_btn.config(text='Search',command=search_password)
search_btn.grid(row=1,column=2)

generate_btn = Button()
generate_btn.config(text='Generate Password',command=generate_password)
generate_btn.grid(row=3,column=2)

add_btn = Button()
add_btn.config(text='Add',width=36,command=save_details)
add_btn.grid(row=4,column=1,columnspan=2)

window.mainloop()