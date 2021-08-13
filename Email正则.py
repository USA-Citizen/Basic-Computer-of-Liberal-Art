from tkinter import *
import re

root = Tk()
root.title('E_mail Test')
root.geometry('560x500')

p = re.compile('^[a-zA-Z0-9]{1,16}@[a-zA-Z0-9]{1,10}.(org|com)$', re.I)
def test():
    s = et.get()
    if s == '0':
        root.destroy()
    else:
        m = p.match(s)
        if m:
            lb.config(text = 'Please input your E-mail that you wish to identify\
    (input \'0\' to exit):\nYour E-mail is regular.')
        else:
            lb.config(text = 'Please input your E-mail that you wish to identify\
    (input \'0\' to exit):\nYour E-mail is irregular.')

def retest(event):
    s = et.get()
    if s == '0':
        root.destroy()
    else:
        m = p.match(s)
        if m:
            lb.config(text = 'Please input your E-mail that you wish to identify\
    (input \'0\' to exit):\nYour E-mail is regular.')
        else:
            lb.config(text = 'Please input your E-mail that you wish to identify\
    (input \'0\' to exit):\nYour E-mail is irregular.')

lb = Label(root, text = 'Please input your E-mail that you wish to identify\
    (input \'0\' to exit):\n')
lb.pack()
et = Entry(root)
et.bind('<Return>', retest)
et.pack()
btn = Button(root, text = 'Test', command = test)
btn.pack()
root.mainloop()