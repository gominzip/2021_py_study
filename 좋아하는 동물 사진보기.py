#좋아하는 동물 사진보기
from tkinter import *
def nextimage():
    global current_image #전역변수의 값을 함수 내부에서 변경시킬 때 글로벌사용
    current_image += 1
    if current_image ==3:
        current_image = 0
    label1.configure(image=photo_list[current_image])
    

window=Tk()

photo_list=[]
photo_list.append(PhotoImage(file='야옹이 이미지.gif'))
photo_list.append(PhotoImage(file='야옹이2.gif'))
photo_list.append(PhotoImage(file='야옹이3.gif'))
current_image=0

button1 = Button(window,text='다음 사진', command=nextimage)
label1 = Label(window, image=photo_list[current_image], fg='red')

button1.pack()
label1.pack()

window.mainloop()
