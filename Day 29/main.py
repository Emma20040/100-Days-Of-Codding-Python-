import random
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_entry.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website= website_input.get()
    email = email_entry.get()
    password = password_entry.get()
   
    if len(website) ==0 or len(email)== 0 or len(password) ==0:
        messagebox.showinfo(title="Oops", message="Please make sure that you haven't left any feild empty")
    
    else:
    # messagebox.showinfo(title="Check info", message="Your info")

        is_ok= messagebox.askokcancel(title=website, message=f"these are the details you entered\n Email: {email}\n"
                            f" Password: {password} \n Is it ok to save?")
        
        if is_ok:
            with open("./Day 29/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_entry.delete(0, END)

    
# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Password Manager")
window.config(padx=50, pady=50 )


canvas = Canvas(width=200, height=200, highlightthickness=0)
l_image= PhotoImage(file="./Day 29/logo.png")
canvas.create_image(100, 100, image=l_image )
canvas.grid(column=1, row=0)

website_input= Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_entry= Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "myeamil@gmail.com")

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)


password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry= Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password_button=  Button(text="Generate Pasword", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()