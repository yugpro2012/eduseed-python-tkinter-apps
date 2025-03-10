from tkinter import *
import random

root = Tk()
root.title("Bulls and Cows")
root.geometry("600x800")
root.configure(bg="#f0f0f0")


tries = 15
number = str(random.randint(1000,9999))

while(len(set(number)))!=4:
    number = str(random.randint(1000,9999))


def check(event):
    guess = e.get()
    if guess.isnumeric() and len(guess) == 4 and len(set(guess)) == 4:
        global tries
        tries -= 1
        bulls = 0
        cows = 0
        l2.config(text = "Tries: " + str(tries))
        l3.config(text = "")
        e.delete(0,END)
        for i in range(4):
            if guess[i] == number[i]:
                bulls += 1
            elif guess[i] in number:
                cows += 1
        l4 = Label(root, text= f"{guess} Bulls - {bulls} Cows - {cows}", font=("Arial", 15), fg="#6699CC", bg="white", padx=10, pady=10)
        l4.pack(pady=10)

        if bulls == 4:
            l3.config(text = "You win")
            e.config(state = "disabled")
        elif tries == 0:
            l3.config(text = "Try again")
            e.config(state = "disabled")
    else:
        l3.config(text = "Please Enter a Valid 4 Digit Number")


l1 = Label(root, text="Guess the Secret Number", font=("Arial", 24, "bold"), fg="white", bg="#6699CC", padx=10, pady=10)
l1.pack(pady=20)


l2 = Label(root, text="Tries: 15", font=("Arial", 18), fg="white", bg="#6699CC", padx=10, pady=10)
l2.pack(pady=10)


e = Entry(root, font=("Arial", 14), width=20, justify="center")
e.pack(pady=10)


l3 = Label(root, text="", font=("Arial", 14), fg="#6699CC", bg="#f0f0f0")
l3.pack(pady=20)

root.bind("<Return>", check)
mainloop()