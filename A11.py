from tkinter import *
import random


root = Tk()
root.title("A4")
root.geometry("600x400")
root.resizable(width = False, height = False)


def submit():
    age = 2024-int(e.get())
    lb2.config(text = "Age:" + str(age))



lb1 = Label(root, text = "Enter Your Year Of Birth", )
lb1.pack(pady = 10)

e = Entry(root, width = 25)
e.pack(pady = 10)

button = Button(root, text = "Submit",command = submit, fg = "white", bg = "orange" )
button.pack(pady = 10)

lb2 = Label(root, text = "", )
lb2.pack(pady = 10)

mainloop()











