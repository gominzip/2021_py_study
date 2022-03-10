from tkinter import *
window=Tk()

photo= PhotoImage(file='야옹이 이미지.gif')

label1 = Label(window, text='파이썬 윈도우', image=photo)
label2 = Label(window, text='라벨입니다', font=('궁서체',30), fg='pink', bg='light green')
label1.pack()
label2.pack()
label2.configure(fg='blue') #configure로 수정 가능
label2['text']='종강냥이' #configure없이도 수정 가능


def myFunc():
    value = entry1.get()
    print(value)
    
button1 = Button(window, text='클릭하세요!', command=myFunc)
button1.pack()

entry1 = Entry(window, width=20, bg='light sky blue')
entry1.insert(0, 'ㅇㅅㅇ;;')
entry1.insert(0, '종강 언제함? ')
entry1.pack()

text1 = Text(window, width=30, bg='pink')
text1.insert(1.0, '지금 오전 2시\n')
text1.insert(2.0, '배고파잉')
text1.pack()

print(text1.get(1.0,END))

window.mainloop()
