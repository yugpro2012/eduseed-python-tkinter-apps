from tkinter import *

root = Tk()
root.title("Stopwatch")
root.geometry("400x300")

minute = 0
seconds = 0
paused = True

def countup():
    global seconds, minute, paused
    if not paused:
        seconds+=1
        if seconds == 60:
            seconds = 0 
            minutes += 1
        lb1.config(text = f"{minute:02d}"+":" + f"{seconds:02d}")
        root.after(1000, countup)

def start():
    global paused
    paused = False
    root.after(1000, countup)

def pause():
    global paused
    paused = True

def reset():
    global paused, seconds, minutes
    seconds = 0
    minutes = 0
    lb1.config(text = "00:00")
    paused = True

frame = Frame(root)
frame.pack()

lb1 = Label(frame, text = "00:00", font = ("Helvetica",70, "bold"))
lb1.grid(row = 0, column = 0, columnspan= 3)

sb = Button(frame, text = "Start", font = ("Helvetica",20,), command = start)
sb.grid(row = 1, column = 0)

pb = Button(frame, text = "Pause", font = ("Helvetica",20,), command = pause)
pb.grid(row = 1, column = 1)

eb = Button(frame, text = "Reset", font = ("Helvetica",20,), command = reset)
eb.grid(row = 1, column = 2)

mainloop()