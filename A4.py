from tkinter import * 


root = Tk()
root.title = "A3"
root.geometry("600x400")
root.resizable(width = False, height = False)

def onclick():
    root.destroy()


    
button = Button(root, text = "click me", command = onclick, bg = "orange", fg = "white")
button.pack(pady = 150)


mainloop()