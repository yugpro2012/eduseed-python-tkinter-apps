from tkinter import *

root = Tk()
root.title("Encoder & Decoder")
root.geometry("600x400")

def encode():
    word = e.get()
    answer = ""
    for i in word:
        if i == "Z":
            answer += "A"
        elif i == "z":
            answer += "a"
        else:
            unicode = ord(i)
            unicode += 1
            letter = chr(unicode)
            answer += letter
    label.config(text = answer)
    
def decode():
    word = e.get()
    answer = ""
    for i in word:
        if i == "A":
            answer += "Z"
        elif i == "a":
            answer += "z"
        else:
            unicode = ord(i)
            unicode -= 1
            letter = chr(unicode)
            answer += letter
    label.config(text = answer)
    


e = Entry(root, font=("Arial", 14), width=40)
e.pack(pady=20)

encode = Button(root, text="Encode", font=("Arial", 12), bg="lightblue", width=12, relief=RAISED, borderwidth = 3, command = encode)
encode.pack(pady=10)

decode = Button(root, text="Decode", font=("Arial", 12), bg="lightgreen", width=12, relief=RAISED, borderwidth = 3, command = decode)
decode.pack(pady=10)

label = Label(root, text="", font=("Arial", 14), fg="black")
label.pack(pady=20)

root.mainloop()

