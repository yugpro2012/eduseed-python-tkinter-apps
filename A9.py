from tkinter import *
import random


root = Tk()
root.title("A4")
root.geometry("600x400")
root.resizable(width = False, height = False)
color = ["red", "orange", "blue", "green", "purple", "lightblue"]

def colourchange():
    lb2.config(bg = random.choice(color))
    lb2.after(500, colourchange)

lb1 = Label(root, text = "Yugan", bg = "black", fg = "white")
lb1.pack(pady = 10)


lb2 = Label(root, text = "",fg = "white")
lb2.pack(pady = 10)

colourchange()
mainloop()