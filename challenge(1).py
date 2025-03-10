from tkinter import *


root = Tk()
root.geometry("600x400")

def dt():
    root.config(bg = "#6699CC")
    label1.config(bg = "white", fg = "#6699CC")

def lt():
    root.config(bg = "white")
    label1.config(bg = "#6699CC", fg = "white")


b = Button(root, text="Dark Theme", font=("Arial", 12), bg="#6699CC", fg="white", width=15, relief=RAISED, command = dt, borderwidth=3)
b.pack(pady=10) 

b1 = Button(root, text="Light Theme", font=("Arial", 12), bg="#DCD6D0", fg="#6699CC", width=15, relief=RAISED, command =  lt,borderwidth=3)
b1.pack(pady=20) 

label1 = Label(root, text="Yugan", font=("Arial", 20), fg="black", bg="#f0f0f0",)
label1.pack(pady=20)


mainloop()