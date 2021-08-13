from tkinter import *

root = Tk()
root.title('Mouse Experiment')
root.geometry('320x240')
def show(event):
    x = event.x
    y = event.y
    lb1.config(text = f'Your mouse is located at ({x}, {y})')
    lb2.config(text = f'Your mouse is located at ({x}, {y})')
lb1 = Label(root, text = '', font = ('字体管家乔乔体', 12))
lb2 = Label(root, text = '', font = ('字体管家乔乔体', 12))
lb1.pack()
lb2.pack()
root.bind('<ButtonRelease-1>', show)
root.bind('<ButtonRelease-2>', show)
root.bind('<ButtonRelease-3>', show)
root.mainloop()