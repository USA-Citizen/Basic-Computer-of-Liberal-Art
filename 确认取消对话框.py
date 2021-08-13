from tkinter import *
import tkinter.messagebox

root = Tk()
def choice():
    dialogue = tkinter.messagebox.askokcancel('Please choose', 'Please choose between ok or cancel')
    if dialogue:
        lb.config(text = 'Having chosen')
    else:
        lb.config(text = 'Having canceled')
lb = Label(root, text = 'Click the button')
lb.pack()
btn = Button(root, text = 'Pop the dialogue box', command = choice)
btn.pack()
root.mainloop()