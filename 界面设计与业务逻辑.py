from tkinter import *
from tkinter.ttk import Combobox

class Ui(Frame):
    def __init__ (self, master = None):
        Frame.__init__(self, master)
        self.master.title('四则运算')
        self.master.geometry('320x240')
        self.createWidgets()
    def createWidgets(self):
        self.top = self.winfo_toplevel()
        self.entry1 = Entry(self.top)
        self.entry1.place(relx = 0.1, rely = 0.1, relwidth = 0.3, relheight = 0.1)
        self.entry2 = Entry(self.top)
        self.entry2.place(relx = 0.5, rely = 0.1, relwidth = 0.3, relheight = 0.1)
        self.combo1List = ['加', '减', '乘', '除']
        self.combo1Var = StringVar(value = '加')
        self.combo1 = Combobox(self.top, textvariable = self.combo1Var, \
            values = self.combo1List)
        self.combo1.place(relx = 0.5, rely = 0.5, relwidth = 0.4)
        self.combo1.bind('<<ComboboxSelected>>', self.calc)
        self.label = Label(self.top)
        self.label.place(relx = 0.5, rely = 0.6, relwidth = 0.4, relheight = 0.2)
class App(Ui):
    def __init__ (self, master = None):
        Ui.__init__(self, master)
    def calc(self, event):
        a = float(self.entry1.get())
        b = float(self.entry2.get())
        dic = {0:a+b, 1:a-b, 2:a*b, 3:a/b if b != 0 else '0不能作为除数'}
        c = dic[self.combo1.current()]
        self.label.config(text = c if c == '0不能作为除数' else f'{c:.4f}')

if __name__ == '__main__':
    top = Tk()
    App(top).mainloop()

