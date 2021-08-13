from tkinter import *
import tkinter.colorchooser

root = Tk()
def choice():
    s = tkinter.colorchooser.askcolor()
    g = str(s)
    lb.config(text = g)

lb = Label(root, text = 'Pay attention to the changes of colors')
lb.pack()
btn = Button(root, text = 'Pop the box', command = choice)
btn.pack()
root.mainloop()