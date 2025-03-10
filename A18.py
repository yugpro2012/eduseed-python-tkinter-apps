from tkinter import *
import random

root = Tk()
root.title("Guess the number")
root.resizable(width = False, height = False)

tries = 10
number = random.randint(1, 100)

def check(event):
    global tries
    if  tries > 0:
        guess = int(e.get())
        tries-=1
        lb2.config(text = "Tries = " + str(tries))
        if number == guess:
            lb3.config(text = "You found it :)")
        elif number < guess:
            lb3.config(text = "The number is less than" + str(guess))
        else:
            lb3.config(text = "The number is greater than" + str(guess))
        e.delete(0,END)
lb1 = Label(root, text = "Guess a number between 1 and 100", font = ("Helvetica", 25, "bold"))
lb1.grid(row = 0, column = 0, pady = 10, columnspan = 2)

e = Entry(root, width = 30)
e.grid(row = 1, column = 0, columnspan = 2, pady = 10)

lb2 = Label(root, text = "Tries=10", font = ("Helvetica", 15,))
lb2.grid(row = 2, column = 0, pady = 10, columnspan = 2)

lb3 = Label(root, text = "", font = ("Helvetica", 15,))
lb3.grid(row = 3, column = 0, pady = 10, columnspan = 2)

root.bind("<Return>", check)
mainloop()
