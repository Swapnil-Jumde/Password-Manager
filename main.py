from tkinter import *
from tkinter import messagebox
import random
import json    #json files are from day 30 lecture
import pyperclip #this module helps in copy the password to clipboard
#--------------------------------------------------Constants--------------------------------------------------#
DARK_GREY="#2b3a55"
GREY ="#9388a2"
YELLOW ="#f7f5dd"
FONT_NAME = "Courier"
#----------------------------------------------TO COPY THE GENERATED PASSWORD----------------------------------------------#
def copy_to_clipboard(text):
    pyperclip.copy(text)
#--------------------------------------------------GENERATE PASSWORD--------------------------------------------------#
def generate_password():
    password_entry.delete(0, END)
    letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z"]
    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbol = ['!', '@', '#', '$', '&', '?', '*']

    password_letters = [random.choice(letter) for _ in range(random.randint(5, 6))]
    password_symbol = [random.choice(symbol) for _ in range(random.randint(2, 3))]
    password_number = [random.choice(number) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbol + password_number
    random.shuffle(password_list)

    password_gen = "".join(password_list)
    password_entry.insert(0, password_gen)
#--------------------------------------------------SAVE PASSWORD--------------------------------------------------#
def save():
    website = website_entry.get().title()
    email = username_entry.get()
    password = password_entry.get()

    new_data={
        website: {
            "email":email,
            "password":password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning",message="Oops!!! Some fields are missing or empty.") #it shows pop up massage
    else:
        add = messagebox.askokcancel(title=website ,message=f"Entered details are\n \nEmail: {email} \nPassword: {password} "
                                                      f"\n\nYou want to add these details???" )
        if add:

            try :
                with open("data.json", "r") as data_file:     #this lines are used for adding data in json formatted file

                    data = json.load(data_file) #loading the data or reading
                    data.update(new_data) #updating old data

            except FileNotFoundError: #if file is not present after starting the app then by this exception handling file got created automatically

                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
                    website_entry.delete(0, END)
                    username_entry.delete(0, END)
                    password_entry.delete(0, END)

            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4) #writing or saving the updated data

            finally:
                    website_entry.delete(0, END)
                    username_entry.delete(0, END)
                    password_entry.delete(0, END)
# --------------------------------------------------Search Function--------------------------------------------------#

def search():
    search_website = website_entry.get().title() #getting the website entry box value
    try:
        with open("data.json", "r") as data_file:
            search_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=website_entry.get(),
                            message=f"No Data Found Of the Entry '{website_entry.get()}'")

    else:
        if search_website in search_data:
            messagebox.showinfo(title=website_entry.get(),
                                message=f"Email: {search_data[search_website]['email']} "
                                        f"\nPassword: {search_data[search_website]['password']} "
                                        f"\n\nPassword Copied to Clipboard :)")
            copy_to_clipboard(search_data[search_website]['password']) #this can copy the password that user has searched

        else:
            messagebox.showinfo(title=website_entry.get(),
                                message=f"No Data Found Of the Entry '{website_entry.get()}'")


#--------------------------------------------------UI--------------------------------------------------#
windows = Tk()
windows.config(padx=70, pady=70, bg=YELLOW)
windows.title("PASSWORD MANAGER")

canvas = Canvas(width=100, height=100, bg=YELLOW,highlightthickness=0)  # Setting the window
logo_image = PhotoImage(file="PASSWORD 2.png")  # adding image to a variable by default method
canvas.create_image(50, 50, image=logo_image)
canvas.grid(column=1, row=0)

#Lable
website_lable = Label(text="Website: ",bg=YELLOW, font=(FONT_NAME, 10, "bold"))
website_lable.grid(column=0, row=1)

#Entry
website_entry = Entry(width=15)
website_entry.focus()
website_entry.grid_configure(padx=5, pady=5)
website_entry.grid(column=1, row=1)

#Lable
username_lable = Label(text= "Username/Email: ",bg=YELLOW, font=(FONT_NAME, 10, "bold"))
username_lable.grid(column=0, row=2)

#Entry
username_entry = Entry(width=35)
#username_entry.insert(0, "swapniljumde@gmail.com") #this line will give us the provided email at begining
username_entry.grid_configure(padx=5, pady=5)
username_entry.grid(column=1, row=2, columnspan=2)

#Lable
password_lable = Label(text= "Password: ",bg=YELLOW, font=(FONT_NAME, 10, "bold"))
password_lable.grid(column=0, row=3)


#Entry
password_entry = Entry(width=15)
password_entry.grid_configure(padx=5, pady=5)
password_entry.grid(column=1, row=3)

#Generate Password Button
generate_pass_button = Button(text="Generate Password", fg=DARK_GREY, command=generate_password)
generate_pass_button.grid_configure(padx=5, pady=5)
generate_pass_button.grid(column=2, row=3)

#Add Button
add_button = Button(text= "Add", width=30, fg=GREY, command=save)
add_button.grid(column=1, row=4, columnspan=2)

#Search Button
search_button = Button(text="Search", width=15, fg=DARK_GREY, command = search)
search_button.grid(column=2, row=1)

mainloop()

