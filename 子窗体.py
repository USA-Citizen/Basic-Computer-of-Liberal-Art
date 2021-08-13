""" import """
from tkinter import *

""" Def a func:
Toplevel. Label. Button. """
def newWin():
    newWin = Toplevel(root)
    newWin.title('子窗体')
    newWin.geometry('320x240')
    lb2 = Label(newWin, text = '子窗体', font = ('字体管家乔乔体', 18), fg = 'grey', bg = 'black')
    lb2.place(relx = 0.3, rely = 0.3)
    btn = Button(newWin, text = '退出', command = newWin.destroy)
    btn.place(relx = 0.7, rely = 0.7, relwidth = 0.3, relheight = 0.3)

""" Root. Label. Menu. """
root = Tk()
root.title('根窗体')
root.geometry('320x240')
lb1 = Label(root, text = '主窗体哈哈哈', font = ('字体管家乔乔体', 36))
lb1.pack()
mainmenu = Menu(root)
submenu = Menu(mainmenu)
mainmenu.add_cascade(label = '彩蛋', menu = submenu)
submenu.add_command(label = '创建子窗体', command = newWin)
submenu.add_separator()
submenu.add_command(label = '退出', command = root.destroy)
root.config(menu = mainmenu)
root.mainloop()