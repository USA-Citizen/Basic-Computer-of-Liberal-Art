#导入
from tkinter import *

#函数初始化
def ini():
    ltbx.delete(0,END)
    list_items = ['命运', 'Zen', 'Fuck you!', '千门万户', '教程']
    for item in list_items:
        ltbx.insert(END, item)

#函数添加
def ins():
    if entry.get() != '' and ltbx.curselection() == () :
        ltbx.insert(ltbx.size(), entry.get())
    elif entry.get() != '' and ltbx.curselection() != () :
        ltbx.insert(ltbx.curselection(), entry.get())

#函数删除
def delt():
    if ltbx.curselection() != () :
        ltbx.delete(ltbx.curselection())

#函数修改
def updt():
    if entry.get() != '' and ltbx.curselection() != () :
        selected = ltbx.curselection()[0]
        ltbx.delete(selected)
        ltbx.insert(selected, entry.get())

#函数清空
def clear():
    ltbx.delete(0, END)

#根窗体
root = Tk()
root.title("列表框试验")
root.geometry('320x240')

#框
frm1 = Frame(root, relief = RAISED)
frm1.place(relx = 0.0)
frm2 = Frame(root, relief = GROOVE)
frm2.place(relx = 0.5)

#列表框
ltbx = Listbox(frm1)
ltbx.pack()

#输入框
entry = Entry(frm2)
entry.pack()

#按钮
btnini = Button(frm2, text = '初始化', command = ini)
btnini.pack(fill = X)
btnins = Button(frm2, text = '添加', command = ins)
btnins.pack(fill = X)
btndelt = Button(frm2, text = '删除', command = delt)
btndelt.pack(fill = X)
btnupdt = Button(frm2, text = '修改', command = updt)
btnupdt.pack(fill = X)
btnclear = Button(frm2, text = '清空', command = clear)
btnclear.pack(fill = X)

#主循环
root.mainloop()