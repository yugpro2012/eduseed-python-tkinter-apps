from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("A2")


button1 = Button(root, text = "A1", bg = "orange")
button1.pack(pady = 10)

button2 = Button(root, text = "A2", bg = "red")
button2.pack(pady = 10, side = BOTTOM)

button3 = Button(root, text = "A3", bg = "yellow")
button3.pack(pady = 10, side = LEFT)

button4 = Button(root, text = "A4", bg = "blue")
button4.pack(pady = 10, side = RIGHT)


mainloop()