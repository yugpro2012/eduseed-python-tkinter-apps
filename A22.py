from tkinter import * 

root = Tk()
root.title("Tax")
root.geometry("600x400")

frame = Frame(root)
frame.pack()

def calculate():
    amount = int(e1.get())
    a = int(e2.get())
    n = amount * a / 100
    l3.config(text = "Tax Amount: " + str(n))
    l4.config(text = "Bill Inclusive Of Tax: " + str(n + amount))

l1 = Label(frame, text = "Bill Amount", font = ("Helvetica", "17", "bold",), fg = "#555555")
l1.pack(pady = 10)
 
e1 = Entry(frame)
e1.pack(pady = 2)

l2 = Label(frame, text = "Tax In Percentage", font = ("Helvetica", "17", "bold"), fg =  "#555555")
l2.pack(pady = 10)

e2 = Entry(frame)
e2.pack(pady = 2)

l3 = Label(frame, text = "Tax Amount: ", font = ("Helvetica", "12", "bold"), fg = "#555555")
l3.pack(pady = 5)

l4 = Label(frame, text = "Bill Inclusive Of Tax: ", font = ("Helvetica", "12", "bold"), fg = "#555555")
l4.pack(pady = 5)

b = Button(frame, text = "submit" , font = ("Helvetica", "12", "bold"), fg = "#555555", command = calculate)
b.pack(pady = 5)

mainloop()