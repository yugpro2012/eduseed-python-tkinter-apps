from tkinter import * 
import random

root = Tk()
root.title("Hangman")
root.geometry("600x400")

wordlist = ["BOOK", "DOG", "GAME", "DOCTOR", "GAMING", "SPORTS", "TIGER", "LAPTOP", "MOBILE", "PYTHON", "CHROME", "KEYS"]
random.shuffle(wordlist)

n = 0 
guess = 10
word = ""
dashes = []
misses = []


def newround():
    global wordlist, word, n
    word = wordlist[n]
    for i in range(len(word)):
        dashes.append("_")
    wordl.config(text = dashes)
    misses.clear()
    letterl.config(text = "")
    guess = 10
    guessl.config(text = "Guesses Left: 10")

def check(event):
    global guess , dashes, word, n, misses
    letter = e.get().upper()
    for i in range(len(word)):
        if word[i] == letter:
            dashes[i] = letter
            wordl.config(text = dashes)
            
    if letter not in word:
        if guess > 0:
            guess -= 1
            guessl.config(text = "Guesses Left: " + str(guess))
            misses.append(letter)
            letterl.config(text = misses)
        else:
            e.config(state = "disabled")   
    e.delete(0,END)

    if "_" not in dashes:
        dashes.clear()
        n += 1
        if n<len(wordlist):
            root.after(1000, newround)
        else:
            resultl.config(text = "You saved the hangman")


guessl = Label(root, text = "Guesses Left: 10", font = ("Helvetica", "17", "bold"))
guessl.pack(pady = 10)

letterl = Label(root, text = "", font = ("Helvetica", "17", "bold"))
letterl.pack(pady = 10)

wordl = Label(root, text = "", font = ("Helvetica", "45", "bold"))
wordl.pack(pady = 10)

e = Entry(root)
e.pack(pady =10)

resultl = Label(root, text = "", font = ("Helvetica", "17", "bold"))
resultl.pack(pady = 10)


root.bind("<Return>", check)

newround()
e.focus()
mainloop()