from tkinter import *
import random


root = Tk()
root.title("A4")
root.geometry("600x400")
root.resizable(width = False, height = False)


def oe():
    name = int(e.get())
    if name%2 == 0:
        lb3.config(text = "it is an even number")
    else:
        lb3.config(text = "it is an odd number")

lb1 = Label(root, text = "ODD/EVEN", bg = "black", fg = "white", width = 15, height = 1)
lb1.pack(pady = 10)

lb2 = Label(root, text = "Enter a number:", bg = "black", fg = "white", width = 15, height = 1)
lb2.pack(pady = 10)

e = Entry(root, width = 25)
e.pack(pady = 10)

button = Button(root, text = "Submit", command = oe, fg = "white", bg = "orange")
button.pack(pady = 10)

lb3 = Label(root, text = "", fg = "red", width = 15, height = 1)
lb3.pack(pady = 10)

mainloop()