#导入
from tkinter import *

#函数初始化两个列表框
def ini():
    list_items = ['刑法总论', '法理学', '债权法总论', '犯罪学', '文科计算机专题']
    for item in list_items:
        ltbx1.insert(END, item)
    list_credits = [4.0, 4.0, 3.0, 2.0, 2.0]
    for credit in list_credits:
        ltbx2.insert(END, credit)
    
#函数1
def release1(event):
    s = '你选择了' + ltbx1.get(ltbx1.curselection()) + str(ltbx2.get(ltbx1.curselection())) + '学分\n'
    txt.insert(END, s) #txt在这里是文本框不是字符串

#函数2
def release2(event):
    s = '你选择了' + ltbx1.get(ltbx2.curselection()) + str(ltbx2.get(ltbx2.curselection())) + '学分\n'
    txt.insert(END, s)

#函数3
def clear():
    txt.delete(0.0, END) #函数要写在执行函数的前面

#根窗体
root = Tk()
root.title('联动选课')
root.geometry('640x380')

#框
frm1 = Frame(root)
frm1.place(relx = 0.0)
frm2 = Frame(root)
frm2.place(relx = 0.3)
frm3 = Frame(root)
frm3.place(relx = 0.6)

#列表框
ltbx1 = Listbox(frm1)
ltbx1.bind('<ButtonRelease-1>', release1) #列表框，绑定，鼠标左键释放，执行函数
ltbx1.pack()
ltbx2 = Listbox(frm2)
ltbx2.bind('<ButtonRelease-1>', release2)
ltbx2.pack()

#文本框
txt = Text(frm3)
txt.pack()

#按钮清空
btn = Button(frm3, text = '清空', command = clear)
btn.pack(fill = BOTH)

#初始化
ini()

#主循环
root.mainloop()