from tkinter import *
import random


root = Tk()
root.title("A4")
root.resizable(width = False, height = False)



lb1 = Label(root, text = "Tkinter Grid using Python", font = ("Helvetica", 15) )
lb1.grid(row = 0, column = 0, columnspan = 2)

lb2 = Label(root, text = "Label 1", font = ("Helvetica",10))
lb2.grid(row = 1, column = 0, sticky = W)

lb3 = Label(root, text = "Label 2", font = ("Helvetica",10))
lb3.grid(row = 1, column = 1, sticky = E)

button = Button(root, text = "Submit", )
button.grid(row = 2, column = 0, columnspan = 2)

mainloop()
