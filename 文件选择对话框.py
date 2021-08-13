from tkinter import *
import tkinter.filedialog

root = Tk()
def choice():
    s = tkinter.filedialog.askopenfilenames()
    if s != '':
        lb.config(text = f'You have chosen {s}')
    else:
        lb.config(text = 'You have not chosen any files')

lb = Label(root, text = 'Click the button')
lb.pack()
btn = Button(root, text = 'Pop the dialogue box', command = choice)
btn.pack()
root.mainloop()