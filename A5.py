from tkinter import * 


root = Tk()
root.title("A4")
root.geometry("600x400")
root.resizable(width = False, height = False)


def addlabel():
    lb = Label(root, text = "new label", bg = "black", fg = "white")
    lb.pack(pady = 10)

button = Button(root, text = "add label", command = addlabel, bg = "orange", fg = "white")
button.pack(pady = 20)


mainloop()