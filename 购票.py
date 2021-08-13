# Import
from tkinter import *

# Root
root = Tk()
root.title('Purchasing Tickets')
root.geometry('560x560')

# Func
def wrt():
    dic = {1: 150, 2: 49, 3: 78}
    price = dic.get(varrb.get())
    if etr.get() != '':
        num = int(etr.get())
        if num >= 50:
            result = 0.8*price*num
        elif 20<= num < 50:
            result = 0.95*price*num
        else:
            result = price*num
        txt.insert(END, f'You have purchased {num} tickets. The total cost will be ¥{result: .2f}.\n')

def clr():
    txt.delete(0.0, END)

# Label1
lb1 = Label(root, text = 'Choose a place you intend to visit:')
lb1.pack()

# RadioButton
varrb = IntVar()
rb1 = Radiobutton(root, text = 'Aquarium', variable = varrb, value = 1)
rb1.pack()
rb2 = Radiobutton(root, text = 'Mountain', variable = varrb, value = 2)
rb2.pack()
rb3 = Radiobutton(root, text = 'Museum', variable = varrb, value = 3)
rb3.pack()

# Label2
lb2 = Label(root, text = 'Input your number of tickets:')
lb2.pack()

# Entry
etr = Entry(root)
etr.pack()

# Button1, 2
btn1 = Button(root, text = 'Count', command = wrt)
btn1.pack()
btn2 = Button(root, text = 'Clear', command = clr)
btn2.pack()

# Text(insert/delete)
txt = Text(root)
txt.pack(fill = BOTH)

# Mainloop
root.mainloop()