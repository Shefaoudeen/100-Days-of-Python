from tkinter import *

window = Tk()
window.title('First GUI Program')
window.minsize(width=500,height=300)

my_label = Label(text="I am a label", font=('Arial',24,'bold'))
my_label.grid(row=0,column=0)

my_label['text'] = "New text"
my_label.config(text="New Text")


def button_clicked():
    new_text = input_label.get()
    my_label.config(text=new_text)


button = Button(text="click me",command=button_clicked)
button.grid(row=1,column=1)

input_label = Entry(width=10)
input_label.grid(row=2,column=3)
print(input_label.get())

button = Button(text="New button")
button.grid(row=0,column=2)

window.mainloop()
