from tkinter import *
import time
import datetime

def gettime():
	s = str(datetime.datetime.now()) + '\n'
	txt.insert(END,s)
	root.after(1000, gettime)
	
root = Tk()
root.title('Clock')
root.geometry('420x420')
txt = Text(root, fg = '#9c3ee5', font = ('Curlz MT', 15))
txt.pack()
gettime()
root.mainloop()