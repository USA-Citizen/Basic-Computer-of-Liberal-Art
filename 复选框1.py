from tkinter import *

def run():
    if (CheckVar1.get() == 0 and CheckVar2.get() == 0 \
        and CheckVar3.get() == 0 and CheckVar4.get() == 0) :
        s = "您没有选择任何书目。"
    else:
        s1 = "《毛泽东选集》" if CheckVar1.get() == 1 else ""        
        s2 = "《德国民法典》" if CheckVar2.get() == 1 else "" 
        s3 = "《朝花夕拾》" if CheckVar3.get() == 1 else ""
        s4 = "《海底两万里》" if CheckVar4.get() == 1 else ""
        s = "您选择了"+f"{s1}{s2}{s3}{s4}。"
    lb2.config(text = s)

root = Tk()
root.title('复选框选择书目')
root.geometry('600x600')

lb1 = Label(root, text = "请选择您喜欢的书目。", font = ('汉仪清韵体简', 16))
lb1.pack()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
ch1 = Checkbutton(root, text = "《毛泽东选集》", variable = CheckVar1, onvalue = 1, offvalue = 0, font = ('汉仪清韵体简', 16))
ch2 = Checkbutton(root, text = "《德国民法典》", variable = CheckVar2, onvalue = 1, offvalue = 0, font = ('汉仪清韵体简', 16))
ch3 = Checkbutton(root, text = "《朝花夕拾》", variable = CheckVar3, onvalue = 1, offvalue = 0, font = ('汉仪清韵体简', 16))
ch4 = Checkbutton(root, text = "《海底两万里》", variable = CheckVar4, onvalue = 1, offvalue = 0, font = ('汉仪清韵体简', 16))
ch1.pack()
ch2.pack()
ch3.pack()
ch4.pack()

btn = Button(root, text = 'OK', command = run)
btn.pack()
lb2 = Label(root, text = '', font = ('汉仪清韵体简', 16))
lb2.pack()
root.mainloop()