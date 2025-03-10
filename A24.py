from tkinter import *

root = Tk()
root.title("Encoder & Decoder")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

def fahrenheit():
    try:
        celsius_value = float(e.get())
        fahrenheit_value = (celsius_value * 9/5) + 32
        result_label.config(text=f"{celsius_value} °C = {fahrenheit_value:.2f} °F")
    except ValueError:
        result_label.config(text="Please enter a valid number")

def celcius():
    try:
        fahrenheit_value = float(e.get())
        celsius_value = (fahrenheit_value - 32) * 5/9
        result_label.config(text=f"{fahrenheit_value} °F = {celsius_value:.2f} °C")
    except ValueError:
        result_label.config(text="Please enter a valid number")

label = Label(root, text="Enter a temperature in Fahrenheit or Celsius", font=("Arial", 14), fg="black", bg="#f0f0f0")
label.pack(pady=20)

e = Entry(root, font=("Arial", 14), width=40, borderwidth=2)
e.pack(pady=20)

fahrenheit_l = Button(root, text="Fahrenheit", font=("Arial", 12), bg="#87CEEB", fg="white", width=15, relief=RAISED, borderwidth=3, command=fahrenheit)
fahrenheit_l.pack(pady=10)

celcius_l = Button(root, text="Celsius", font=("Arial", 12), bg="#32CD32", fg="white", width=15, relief=RAISED, borderwidth=3, command=celcius)
celcius_l.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 14), fg="black", bg="#f0f0f0")
result_label.pack(pady=20)

root.mainloop()
