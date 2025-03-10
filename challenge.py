from tkinter import *
from tkinter.ttk import Combobox  

root = Tk()
root.geometry("600x400")
root.title("Space Weight (Challenge)")  


planets_l = ['Mercury', 'Venus','Mars', 'Jupiter', "Saturn", 'Uranus', "Neptune"]

def calculate():
    planet = planets.get()
    weight = int(e.get())

    if planet == "Mercury":  
        label2.config(text = weight*0.38)

    if planet == "Venus":  
        label2.config(text = weight*0.91)

    if planet == "Mars":  
        label2.config(text = weight*0.38)

    if planet == "Jupiter":  
        label2.config(text = weight*2.34)

    if planet == "Saturn":  
        label2.config(text = weight*0.93)

    if planet == "Uranus":  
        label2.config(text = weight*0.92)

    if planet == "Neptune":  
        label2.config(text = weight*1.12)



label = Label(root, text="Weight (in kg)", font=("Arial", 14), fg="black", bg="#f0f0f0")
label.pack(pady=20)

e = Entry(root, font=("Arial", 14), width=40)
e.pack(pady=20)

label1 = Label(root, text="Planets in the Solar System", font=("Arial", 14), fg="black", bg="#f0f0f0")
label1.pack(pady=20)

planets = Combobox(root, values = planets_l, state="readonly")
planets.pack(pady=10)

b = Button(root, text="Check", font=("Arial", 12), bg="#87CEEB", fg="white", width=15, relief=RAISED, borderwidth=3, command = calculate)
b.pack(pady=10) 

label2 = Label(root, text="", font=("Arial", 14), fg="black", bg="#f0f0f0")
label2.pack(pady=20)

mainloop()
