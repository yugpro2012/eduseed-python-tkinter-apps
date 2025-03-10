from tkinter import * 
import random

root = Tk()
root.title("A4")
root.geometry("600x400")
root.resizable(width = False, height = False)
color = ["red", "orange", "blue", "green", "purple", "lightblue"]


def changecolour():
    root.config(bg = random.choice(color))
    root.after(1000, changecolour)


changecolour()
mainloop()