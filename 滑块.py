"""Create a scale.

    """

# 导入
from tkinter import *

# 根窗体
root = Tk()
root.title('滑块')
root.geometry('640x480')

# 函数显示数值
def show(event):
    s = '当前数值为' + str(var.get())
    lb.config(text = s)

# 滑块
var = DoubleVar() # 滑块的浮点数型变量
scl = Scale(root, width = 20, length = 400, orient = VERTICAL, from_ = -20.00, to = 20.00,
    tickinterval = 2.00, resolution = 0.02, label = '请移动滑块', variable = var) # 滑块只有label没有text
scl.bind('<ButtonRelease-1>', show)
scl.pack()

# 标签
lb = Label(root, text = '当前数值为')
lb.pack()

# 主循环
root.mainloop()