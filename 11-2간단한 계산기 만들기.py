#간단한 계산기 만들기
from tkinter import*

#클릭함수 정의
def click7():
    display.insert(END, '7')
def click8():
    display.insert(END, '8')
def click9():
    display.insert(END, '9')
def click_division():
    display.insert(END, '/')
def click_clear():
    display.delete(0,END)
    
def click4():
    display.insert(END, '4')
def click5():
    display.insert(END, '5')
def click6():
    display.insert(END, '6')
def click_multi():
    display.insert(END, '*')
def click_no_user1():
    pass

def click1():
    display.insert(END, '1')
def click2():
    display.insert(END, '2')
def click3():
    display.insert(END, '3')
def click_minus():
    display.insert(END, '-')
def click_no_user2():
    pass

def click0():
    display.insert(END, '0')
def click_dot():
    display.insert(END, '.')
def click_result():   #결과값 내기
    result=eval(display.get())
    click_clear()
    display.insert(0,result)
def click_plus():
    display.insert(END, '+')
def click_no_user3():
    pass

#쉽게 하는 법
def click(x):
    display.insert(END, x)
#그 뒤에 람다표현식(이름이 없는 함수) 사용, ex) command=lambda:click('7')

window=Tk()
window.title('계산기')

display =Entry(window, width=33, bg="yellow")

btn7=Button(window, text='7', width=5, command=lambda:click('7')) #람다표현식 예시
btn8=Button(window, text='8', width=5, command=lambda x=8:click(x)) #함수의 기본값을 8로 지정해서 작성도 ㄱㄴ
btn9=Button(window, text='9', width=5, command=click9)
btn_division=Button(window, text='/', width=5, command=click_division)
btn_clear=Button(window, text='C', width=5, command=click_clear)

btn4=Button(window, text='4', width=5, command=click4)
btn5=Button(window, text='5', width=5, command=click5)
btn6=Button(window, text='6', width=5, command=click6)
btn_multi=Button(window, text='*', width=5, command=click_multi)
btn_no_user1=Button(window, text=' ', width=5, command=click_no_user1)

btn1=Button(window, text='1', width=5, command=click1)
btn2=Button(window, text='2', width=5, command=click2)
btn3=Button(window, text='3', width=5, command=click3)
btn_minus=Button(window, text='-', width=5, command=click_minus)
btn_no_user2=Button(window, text=' ', width=5, command=click_no_user2)

btn0=Button(window, text='0', width=5, command=click0)
btn_dot=Button(window, text='.', width=5, command=click_dot)
btn_result=Button(window, text='=', width=5, command=click_result)
btn_plus=Button(window, text='+', width=5, command=click_plus)
btn_no_user3=Button(window, text=' ', width=5, command=click_no_user3)

#위젯배치
display.grid(row=0, column=0, columnspan=5)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn_division.grid(row=1, column=3)
btn_clear.grid(row=1, column=4)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn_multi.grid(row=2, column=3)
btn_no_user1.grid(row=2, column=4)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn_minus.grid(row=3, column=3)
btn_no_user2.grid(row=3, column=4)

btn0.grid(row=4, column=0)
btn_dot.grid(row=4, column=1)
btn_result.grid(row=4, column=2)
btn_plus.grid(row=4, column=3)
btn_no_user3.grid(row=4, column=4)

window.mainloop()
