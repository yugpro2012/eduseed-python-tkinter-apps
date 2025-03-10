from tkinter import *
import random


root = Tk()
root.title("Stop Watch")
root.geometry("600x400")
root.resizable(width = False, height = False)


time = 10

def cd():
    global time
    time -= 1
    lb1.config(text = "Time:"+str(time))
    if time > 0:
        root.after(1000,cd)

lb1 = Label(root, text = "Time:10", font = ("Helvetica", 15) )
lb1.pack(pady = 10)


cd()


mainloop()
