from tkinter import *


root = Tk()
root.title = "MY FIRST PROJECT"
root.geometry("600x400")
root.resizable(width = False, height = False)


button1 = Button(root, text = "click",)
button1.pack(pady = 20)

button2 = Button(root, text = "click", )
button2.pack(pady = 20)

button3 = Button(root, text = "click", )
button3.pack(pady = 20)

button4 = Button(root, text = "click", )
button4.pack(pady = 20)


mainloop()