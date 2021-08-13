import time
import tkinter

def gettime():
	var.set(time.strftime('%Y:%m:%d:%H:%M:%S'))
	root.after(1000, gettime)
	
root = tkinter.Tk()
root.title = 'Clock'
var = tkinter.StringVar()

lb = tkinter.Label(root, textvariable = var, fg = '#9c3ee5', font = ('Curlz MT', 32))
lb.pack()
gettime()
root.mainloop()