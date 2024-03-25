from tkinter import *

text_size = 15

window = Tk()
window.config(padx=20,pady=20)
window.title('Mile to Km Converter')

miles = Entry(font=('Arial',text_size))
miles.config(width=10)
miles.grid(row=0, column=1)

miles_text = Label(text="Miles",font=('Arial',text_size,'bold'))
miles_text.grid(row=0, column=2)

equal_text = Label(text="is equal to",font=('Arial',text_size))
equal_text.grid(row=1, column=0)

km = Label(text="0",font=('Arial',text_size))
km.grid(row=1, column=1)

km_text = Label(text="Km",font=('Arial',text_size,'bold'))
km_text.grid(row=1, column=2)

def calculate_km():
    mile = int(miles.get())
    equ_km = round(mile*1.609344,2)
    km.config(text=str(equ_km))


calculate = Button(text="Calculate",font=('Arial',text_size,'bold'),command=calculate_km)
calculate.grid(row=2,column=1)

window.mainloop()
