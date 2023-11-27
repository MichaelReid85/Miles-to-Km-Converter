from tkinter import *
import math

window = Tk()
window.title("Miles to Km Converter")
window.minsize(500, 500)
window.config(padx=90, pady=150)


def button_clicked():
    conversion.config(text=math.floor(int(input.get()) * 1.609344))


input = Entry(width=7)
input.insert(END, string="0")
input.focus()
input.grid(column=1, row=0)

miles = Label(text="Miles", font=("Ariel", 20))
miles.grid(column=2, row=0)

equals = Label(text="is equal to", font=("Ariel", 20))
equals.grid(column=0, row=1)

conversion = Label(text="0", font=("Ariel", 20))
conversion.grid(column=1, row=1)
conversion.config(padx=20, pady=20)

km = Label(text="Km", font=("Ariel", 20))
km.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
