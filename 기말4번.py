from tkinter import *

window = Tk()
entry1 = Entry(window, width=16)
btn1 = Button(window, width=4, height=5, text="BTN1")
btn2 = Button(window, width=10, height=1, text="BTN2")
btn3 = Button(window, width=4, height=1, text="BTN3")
btn4 = Button(window, width=4, height=1, text="BTN4")
btn5 = Button(window, width=4, height=3, text="BTN5")
label1 = Label(window, width=16, text="LABEL1", bg='white')
entry1.grid(row=0, column=0, columnspan=3)
btn1.grid(row=1, column=0, rowspan=3)
btn2.grid(row=1, column=1, columnspan=2)
btn3.grid(row=2, column=1)
btn4.grid(row=3, column=1)
btn5.grid(row=2, column=2, rowspan=2)
label1.grid(row=4, column=0,columnspan=3)

window.mainloop()
