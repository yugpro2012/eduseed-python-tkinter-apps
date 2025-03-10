from tkinter import *


root = Tk()
root.title("A4")
root.geometry("600x400")
root.resizable(width = False, height = False)

def display():
    name = e.get()
    lb1.config(text = "Hello: " + name)


lb = Label(root, text = "Enter your name", bg = "black", fg = "white")
lb.pack(pady = 10)


e = Entry(root, width = 25)
e.pack(pady = 10)


button = Button(root, text = "Click me", command = display, fg = "white", bg = "orange")
button.pack(pady = 10)

lb1 = Label(root, text = "", bg = "black", fg = "white")
lb1.pack(pady = 10)

mainloop()