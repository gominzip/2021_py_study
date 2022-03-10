from tkinter import *
from tkinter import messagebox #메시지박스 사용을 위한 추가 설정

def myFunc():
    messagebox.showinfo('고양이 버튼', '고양이가 귀엽죠?')

window=Tk()
photo = PhotoImage(file='야옹이2.gif')
button1=Button(window, image=photo, command=myFunc)
button1.pack()
window.mainloop()
