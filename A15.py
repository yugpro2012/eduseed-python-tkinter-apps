from tkinter import *
import random


root = Tk()
root.title("Stop Watch")
root.geometry("600x400")
root.resizable(width = False, height = False)


lb1 = Label(root, text = "Time:10", font = ("Helvetica", 15) )
lb1.pack(pady = 10)

button = Button(root, text = "Submit",command = , fg = "white", bg = "orange" )
button.pack(pady = 10)