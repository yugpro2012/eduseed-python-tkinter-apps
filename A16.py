from tkinter import *
import random


root = Tk()
root.title("Colour game")
root.geometry("600x400")
root.resizable(width = False, height = False)

score = 0
timeleft = 60

colours = ["red","blue","green","yellow","black","brown","white","pink","purple","orange"]

colourchosen = ""


def check(event):
    global score
    if timeleft > 0:
        if e.get() == colourchosen:
            score += 1
            lb2.config(text = "Score: "+str(score))
        e.delete(0, END)
        changecolour()

def cd():
    global timeleft
    timeleft -= 1
    lb3.config(text = "Timeleft: "+str(timeleft))
    if timeleft > 0:
        lb3.after(1000,cd)

def changecolour():
    global colourchosen
    colourchosen = random.choice(colours)
    lb4.config(fg = colourchosen)
    lb4.config(text = random.choice(colours))

lb1 = Label(root, text = "Type in the colour of the words,and not word text!", font = ("Helvetica", 15, "bold") )
lb1.pack(pady = 5)

lb2 = Label(root, text = "Score: 0", font = ("Helvetica", 15, "bold"))
lb2.pack(pady = 5)

lb3 = Label(root, text = "Time-left: 60", font = ("Helvetica", 15, "bold"))
lb3.pack(pady = 5)

lb4 = Label(root, text = "", font = ("Helvetica", 40, "bold"))
lb4.pack(pady = 5)

e = Entry(root)
e.pack(pady = 10)

root.bind('<Return>', check)

changecolour()
lb3.after(1000, cd)
e.focus()
mainloop()