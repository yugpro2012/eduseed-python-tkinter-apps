from tkinter import *

root = Tk()
root.title("Guess the number")
root.resizable(width = False, height = False)

time = 10
score = 0

def countdown():
    global time
    time -= 1
    lb1.config(text = "Time:" + str(time))
    if time > 0:
        lb1.after(1000, countdown)

def buttonclick():
    global score
    if time > 0: 
        score += 1
        lb2.config(text = "Score: " + str(score))
        
root = Tk()
root.title("Guess the number")
root.resizable(width = False, height = False)

lb1 = Label(root, text = "Time: 10", font = ("Helvetica",20, "bold"))
lb1.grid(row = 0, column = 0, columnspan= 2, pady = 10)

lb2 = Label(root, text = "Score: 0", font = ("Helvetica",20, "bold"))
lb2.grid(row = 1, column = 0, columnspan= 2, pady = 10)

b = Button(root, text = "Submit",command = buttonclick)
b.grid(row = 2, column = 0, columnspan= 2, pady = 10)
root.after(1000,countdown)
mainloop()