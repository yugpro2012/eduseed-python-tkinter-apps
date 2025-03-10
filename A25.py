from tkinter import *
import random

root = Tk()
root.title("Wordle")
root.geometry("600x400")



wordlist = ['ABODE', 'ALERT', 'ANGRY', 'AUDIO', 'AVOID', 'BAKER', 'BLAME', 'BLEND', 
            'BREAD', 'BRAIN', 'BRAKE', 'BRAVE', 'CABIN', 'CHASE', 'CLEAN', 'CLIMB', 
            'CLOUD', 'CRAFT', 'CRANE', 'CREAM', 'DANCE', 'DELTA', 'DRAKE', 'DRIVE', 
            'EIGHT', 'FAULT', 'FLAME', 'FOCUS', 'FOUND', 'FRANK', 'GLOBE', 'GRAIN', 
            'GRAND', 'GRAPE', 'HATCH', 'HOUSE', 'HOVER', 'INDEX', 'JOLLY', 'KNIFE', 
            'LABEL', 'LEARN', 'LEMON', 'MARCH', 'MIGHT', 'MOUSE', 'NIGHT', 'OCEAN', 
            'PAINT', 'PEARL', 'PRAWN', 'PROUD', 'QUIET', 'QUILT', 'RADIO', 'RAISE', 
            'REACH', 'RIGHT', 'SHARK', 'SIGHT', 'SPARK', 'STEAM', 'STORK', 'TEACH', 
            'THROW', 'TIGER', 'TOPIC', 'TRACE', 'TRACK', 'TRAIN', 'TRICK', 'ULTRA', 
            'UNDER', 'VALUE', 'VIDEO', 'VOICE', 'WASTE', 'WHALE', 'WHITE', 'WHOLE', 
            'WHEAT', 'WORTH', 'XYLEM', 'ZEBRA', 'ZONAL', 'BLOAT', 'CLASH', 'DAUNT', 
            'FIERY', 'GLINT', 'HURRY', 'JUMPS', 'KNACK', 'LUSTY', 'MORAL', 'NERVE', 
            'PLANT', 'QUIRK', 'ROUND', 'SHOUT', 'THUMP', 'VAULT', 'WIELD', 'BLUFF', 
            'CRISP', 'GLARE', 'PLUCK', 'SPADE', 'TWIRL', 'ZONED']


word = random.choice(wordlist)
tries = 6

def check(event):
    global word, tries
    guess = e.get().upper()
    if len(guess) == 5 and guess.isalpha() and len(set(guess)) == 5:
        tries -= 1
        correct = 0
        e.delete(0,END)
        frame = Frame(root)
        for i in range(5):
            if guess[i] == word[i]:
                correct += 1
                label = Label(frame,text = guess[i], fg = "green", font = ("Helvetica", 30, "bold"))
                label.grid(row = 0, column = i) 
            elif guess[i] in word:
                label = Label(frame,text = guess[i], fg = "yellow", font = ("Helvetica", 30, "bold"))
                label.grid(row = 0, column = i)
            else:
                label = Label(frame,text = guess[i], fg = "gray", font = ("Helvetica", 30, "bold"))
                label.grid(row = 0, column = i)
        frame.pack()

        if correct == 5:
            win_label = Label(root,text ="You Win", fg = "blue", bg = "orange")
            win_label.pack(pady = 10)
            e.config(state = "disabled")
        elif tries == 0:
            lost_label = Label(root,text ="Try Again", fg = "blue", bg = "orange")
            lost_label.pack(pady = 10)
            e.config(state = "disabled")


root.bind("<Return>", check)

title = Label(root, text="Guess the 5-letter word in 6 tries", font=("Arial", 14), fg="black", bg="#f0f0f0")
title.pack(pady=20)

e = Entry(root, font=("Arial", 14), width=40, borderwidth=2)
e.pack(pady=20)


mainloop()