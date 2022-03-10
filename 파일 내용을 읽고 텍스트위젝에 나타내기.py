#파일 내용을 읽고 텍스트위젝에 나타내기
from tkinter import*
from tkinter import messagebox

def readfile():
    text1.delete(1.0,END)
    with open('새파일.txt','r') as f:
        data = f.read()
    text1.insert(1.0, data)

def writefile():
    data =text1.get(1.0,END)
    with open('새파일.txt','w') as f:
        f.write(data)
    messagebox.showinfo('알림', '저장되었습니다.')


window=Tk()
text1=Text(window, width=40, height=20, bg='white')
button1 =Button(window, text='파일 불러오기!', command=readfile)
button2 =Button(window, text='파일 저장하기!', command=writefile)

text1.pack()
button1.pack()
button2.pack()
window.mainloop()
