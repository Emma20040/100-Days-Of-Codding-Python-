from tkinter import *
window= Tk()
window.title("My GUI Program")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

def button_listener():
    # print('thanks for licking on the link!!')
    new_text = input.get()
    my_label.config(text= new_text)

# Label
my_label = Label(text="this is a label", font=('Arial', 24, 'bold' ))

my_label.config(text='new text')
# my_label.place(x=110, y=0)
my_label.grid(column=0, row=0)

# button


button =Button(text='click here', command=button_listener)
button.grid(column=1, row=1)

new_button = Button(text='new button')
new_button.grid(column=2, row=0)

# entry
input = Entry(width= 10)

print(input.get())


window.mainloop()