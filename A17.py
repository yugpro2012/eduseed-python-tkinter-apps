from tkinter import *
import random

root = Tk()
root.title("Word Unscrambler")
root.resizable(width = False, height = False)

wordlist = ["BOOK", "DOG", "GAME", "DOCTOR", "GAMING", "SPORTS", "PEACOCK", "TIGER", "LAPTOP", "MOBILE", "PYTHON", "TKINTER", "CHROME", "KEYS"]
random.shuffle(wordlist)

score = 0
time = 0
word = ""
n = 0
completed = False

def jumble():
    global word
    word = wordlist[n]
    j = random.sample(word, len(word))
    lb4.config(text = j)
    
def check(event):
    global score, n, completed, word
    if e.get().upper() == word and not completed:
        score += 1
        lb2.config(text = "Score: " + str(score))
        e.delete(0,END)
        n += 1
        if n<len(wordlist):
            jumble()
        else:
            completed = True
            lb5.config(text = "You have completed this game in " +str(time) + " seconds")

def count():
    global time, completed
    if not completed:
        time += 1
        lb3.config(text = "Time: "+str(time))
        root.after(1000,count)

    

lb1 = Label(root, text = "Unscrable the word in the shortest time possible!", font = ("Helvetica", 15, "bold"))
lb1.grid(row = 0, column = 0, pady = 10, columnspan = 2)

lb2 = Label(root, text = "Score: 0", font = ("Helvetica",15, "bold"))
lb2.grid(row = 1, column = 0, sticky = W, pady = 10)

lb3 = Label(root, text = "Time: 0", font = ("Helvetica",15, "bold"))
lb3.grid(row = 1, column = 1, sticky = E, pady = 10)

lb4 = Label(root, text = "", font = ("Helvetica",40, "bold"))
lb4.grid(row = 2, column = 0, columnspan = 2, pady = 10)

e = Entry(root)
e.grid(row = 3, column = 0, columnspan = 2, pady = 10)

lb5 = Label(root, text = "", font = ("Helvetica",15, "bold"))
lb5.grid(row = 4, column = 0, columnspan = 2, pady = 10)

jumble()
root.bind("<Return>", check)
e.focus()
root.after(1000, count)
mainloop()