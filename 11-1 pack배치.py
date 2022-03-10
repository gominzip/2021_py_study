from tkinter import*
window=Tk()
window.title('고정위치 배치하기')
window.geometry('210x210')

btnList=[]
btnList.append(Button(window, text="버튼1"))
btnList.append(Button(window, text="버튼2"))
btnList.append(Button(window, text="버튼3"))

btnList[0].grid(row=0,column=0)
btnList[1].grid(row=1,column=1)
btnList[2].grid(row=2,column=2)
window.mainloop
 
