from tkinter import *

# 函数响应菜单选择
def new():
    s = '新建'
    lb.config(text = s)
def opn():
    s = '打开'
    lb.config(text = s)
def sav():
    s = '保存'
    lb.config(text = s)
def cut():
    s = '剪切'
    lb.config(text = s)
def cop():
    s = '复制'
    lb.config(text = s)
def pst():
    s = '粘贴'
    lb.config(text = s)
def popumenu(event):
    mainmenu.post(event.x_root, event.y_root)

# 根窗体
root = Tk()
root.title('菜单')
root.geometry('560x560')

# 菜单分组
mainmenu = Menu(root)
menuFile = Menu(mainmenu)
mainmenu.add_cascade(label = '文件', menu = menuFile)
menuFile.add_command(label = '新建', command = new)
menuFile.add_command(label = '打开', command = opn)
menuFile.add_command(label = '保存', command = sav)
menuFile.add_separator()
# root.destroy关闭窗体
menuFile.add_command(label = '退出', command = root.destroy)
menuEdit = Menu(mainmenu)
mainmenu.add_cascade(label = '编辑', menu = menuEdit)
menuEdit.add_command(label = '剪切', command = cut)
menuEdit.add_command(label = '复制', command = cop)
menuEdit.add_command(label = '粘贴', command = pst)

# 标签
lb = Label(root, text = '', font = ('字体管家乔乔体', 50))
lb.pack(fill = BOTH)

# 快捷菜单
root.config(menu = mainmenu)
root.bind('<Button-3>', popumenu)
root.mainloop()