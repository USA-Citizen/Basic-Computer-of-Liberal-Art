from tkinter import *
import tkinter.simpledialog

root = Tk()
def choice():
    s = tkinter.simpledialog.askstring('Please choose', 'Please imput a string')
    lb.config(text = s)

lb = Label(root, text = 'Click the button')
lb.pack()
btn = Button(root, text = 'Pop the dialogue box', command = choice)
btn.pack()
root.mainloop()