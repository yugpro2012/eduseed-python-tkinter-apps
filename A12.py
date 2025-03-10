from tkinter import *
import random


root = Tk()
root.title("A4")
root.resizable(width = False, height = False)



lb1 = Label(root, text = "Username:", )
lb1.grid(row = 0, column = 0)

lb2 = Label(root, text = "Username:", )
lb2.grid(row = 1, column = 0)

e = Entry(root, width = 25)
e.grid(row = 0, column = 1)

e = Entry(root, width = 25)
e.grid(row = 1, column = 1)

button = Button(root, text = "Submit", )
button.grid(row = 2, column = 1)


mainloop()