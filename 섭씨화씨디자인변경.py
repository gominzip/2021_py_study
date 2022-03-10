from tkinter import *

def CtoF():
    entry2.delete(0,END)
    c= float(entry1.get())
    F= (c*1.8)+32
    entry2.insert(0, F)

window=Tk()
label1 = Label(window, text='섭씨')
label1.grid(row=0,column=0)
entry1 = Entry(window, width=20, bg='light green')
entry1.grid(row=0,column=1)

label2= Label(window, text='화씨')
label2.grid(row=1,column=0)
entry2 = Entry(window, width=20, bg='pink')
entry2.grid(row=1,column=1)

button1 = Button(window, text='섭씨->화씨', command=CtoF)
button1.grid(row=0,column=3,rowspan=2)

window.mainloop()
