from tkinter import *


root = Tk()
root.title("BMI Calculator")
root.geometry("600x400")

def calculate():
    weight = int(e.get())
    height = int(e1.get())

    BMI = weight/height**2

    label4.config(text = BMI)

    if BMI < 18.5:
        label3.config(text = "Underweight")

    if BMI > 18.5 and BMI < 24.9:
        label3.config(text = "Normal weight")

    if BMI > 25 and BMI < 30:
        label3.config(text = "Normal weight")

    if BMI > 30:
        label3.config(text = "Obese")


label1 = Label(root, text="Weight", font=("Arial", 20), fg="#6699CC", bg="white",)
label1.pack(pady=20)

e = Entry(root, font=("Arial", 14), width=40, borderwidth=2)
e.pack(pady=20)

label2 = Label(root, text="Height(in meters)", font=("Arial", 20), fg="white", bg="#6699CC",)
label2.pack(pady=20)

e1 = Entry(root, font=("Arial", 14), width=40, borderwidth=2)
e1.pack(pady=20)

b = Button(root, text="Celsius", font=("Arial", 12), bg="#32CD32", fg="white", width=15, relief=RAISED, borderwidth=3, command=calculate)
b.pack(pady=20)

label4 = Label(root, text="", font=("Arial", 20), fg="white", bg="#6699CC",)
label4.pack(pady=20)

label3 = Label(root, text="", font=("Arial", 20), fg="white", bg="#6699CC",)
label3.pack(pady=20)

mainloop()