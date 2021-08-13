from tkinter import *

root = Tk()
root.title('Keyboard Experiment')
root.geometry('320x240')
def show(event):
    s = event.keysym
    lb.config(text = s)
lb = Label(root, text = '', font = ('字体管家乔乔体', 30))
lb.bind('<Key>', show)
lb.focus_set()
lb.pack()
root.mainloop()