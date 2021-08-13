#导入tkinter
from tkinter import *

#函数确定
def run():
    dic = {0:'', 1:'《我和我的祖国》', 2:'《德意志意识形态》', 3:'《法律的正当程序》', 4:'《聊斋志异》'}
    lst = [CheckVar1.get(), CheckVar2.get(), CheckVar3.get(), CheckVar4.get()]
    s = ''
    for i in lst:
        s += dic.get(i)
    if s == '':
        s = '你没有选择任何书目。'
    else:
        s = '你选择了'+s+'。'
    lb2.config(text = s)

#函数全选
def all():
    ch1.select()
    ch2.select()
    ch3.select()
    ch4.select()

#函数重置
def cancel():
    ch1.deselect()
    ch2.deselect()
    ch3.deselect()
    ch4.deselect()

#函数反选
def invert():
    ch1.toggle()
    ch2.toggle()
    ch3.toggle()
    ch4.toggle()

#根窗体
root = Tk()
root.title('复选框选择书目')
root.geometry('840x420')

#标签
lb1 = Label(root, text = '请选择你的书目。', font = ('汉仪苏泽立行楷原版W', 14))
lb1.pack()

#复选框
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
ch1 = Checkbutton(root, text = '《我和我的祖国》', font = ('汉仪苏泽立行楷原版W', 14), \
    variable = CheckVar1, onvalue = 1, offvalue = 0)
ch2 = Checkbutton(root, text = '《德意志意识形态》', font = ('汉仪苏泽立行楷原版W', 14), \
    variable = CheckVar2, onvalue = 2, offvalue = 0)
ch3 = Checkbutton(root, text = '《法律的正当程序》', font = ('汉仪苏泽立行楷原版W', 14), \
    variable = CheckVar3, onvalue = 3, offvalue = 0)
ch4 = Checkbutton(root, text = '《聊斋志异》', font = ('汉仪苏泽立行楷原版W', 14), \
    variable = CheckVar4, onvalue = 4, offvalue = 0)
ch1.pack()
ch2.pack()
ch3.pack()
ch4.pack()

#按钮
btrun = Button(root, text = '确定选择', font = ('汉仪苏泽立行楷原版W', 14), command = run)
btall = Button(root, text = '全部选择', font = ('汉仪苏泽立行楷原版W', 14), command = all)
btcancel = Button(root, text = '重置选择', font = ('汉仪苏泽立行楷原版W', 14), command = cancel)
btinvert = Button(root, text = '反转选择', font = ('汉仪苏泽立行楷原版W', 14), command = invert)
btrun.pack()
btall.pack()
btcancel.pack()
btinvert.pack()

#标签
lb2 = Label(root, text = '', font = ('汉仪苏泽立行楷原版W', 14))
lb2.pack()

#根窗体主循环
root.mainloop()