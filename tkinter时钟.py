import tkinter
import time 

def gettime():
	timestr = time.strftime("%Y:%m:%d:%H:%M:%S")
	lb.configure(text = timestr)
	root.after(1000, gettime)
	
root = tkinter.Tk()
root.title('Clock')

lb = tkinter.Label(root, text='', fg = '#9c3ee5', font = ('Curlz MT', 32))
lb.pack()
gettime()
root.mainloop()