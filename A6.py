from tkinter import * 
import random


root = Tk()
root.title("A4")
root.geometry("600x400")
root.resizable(width = False, height = False)


color = ["red", "orange", "blue", "green", "purple", "lightblue"] 

def change():
    button.config(bg = random.choice(color))

button = Button(root, text = "change colour", command = change, fg = "white")
button.pack(pady = 20)


mainloop()