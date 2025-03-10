from tkinter import * 


root = Tk()
root.title = "A3"
root.geometry("600x400")
root.resizable(width = False, height = False)

def onclick():
    label.config(text = "button clicked")

def onclick1():
    label.config(text = "")

def onclick2():
    label1.config(text = "You are locked in")

label = Label(root, text = "", bg = "black", fg = "white")
label.pack(pady = 60)

button = Button(root, text = "click me", command = onclick, bg = "orange", fg = "white")
button.pack(pady = 10)


button1 = Button(root, text = "delete", command = onclick1, bg = "orange", fg = "white")
button1.pack(padx = 10)


label1 = Label(root, text = "", bg = "black", fg = "white")
label1.pack(pady = 60)

button2 =  Button(root, text = "click me 1", command = onclick2, bg = "orange", fg = "white")
button2.pack(padx = 10)
mainloop()