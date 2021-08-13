from tkinter import *
root = Tk()
lb1 = Label(root, text = 'Who else is going to have a try?',\
		bg = '#9cf3f0',\
		fg = '#9c3ee5',\
		font = ('Curlz MT',32),\
		height = 6,\
        width = 100,\
        relief = FLAT)
lb1.place(relx = 0.2, rely = 0.2, relheight = 0.6, relwidth = 0.6)
lb2 = Label(root, text = 'Nobody!!',\
		bg = '#9cf3f0',\
		fg = '#9c3ee5',\
		font = ('Curlz MT',32),\
		height = 6,\
        width = 100,\
        relief = FLAT)
lb2.place(relx = 0.2, rely = 0.2, relheight = 0.6, relwidth = 0.6)
root.title('How am I supposed to live?')
root.geometry('1366x768')
root.mainloop()