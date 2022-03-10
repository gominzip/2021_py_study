#GUI 화씨 변환 프로그램
from tkinter import *

def CtoF():
    entry2.delete(0,END)
    c= float(entry1.get())
    F= (c*1.8)+32
    entry2.insert(0, F)

window=Tk()
label1 = Label(window, text='섭씨', width=30)
label1.pack()
entry1 = Entry(window, width=20, bg='light green')
entry1.pack()

label2= Label(window, text='화씨', width=30)
label2.pack()
entry2 = Entry(window, width=20, bg='pink')
entry2.pack()

button1 = Button(window, text='섭씨->화씨', command=CtoF)
button1.pack()

window.mainloop()
