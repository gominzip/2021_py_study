#터틀 객체로 사각형 그리기
width=int(input('사각형의 가로길이를 입력하세요 : '))
length=int(input('사각형의 세로길이를 입력하세요 : '))

#거북이사용설정
import turtle
t = turtle.Pen()
t.shape('turtle')

#사각형 그리기
t.forward(width)
t.right(90)
t.forward(length)
t.right(90)
t.forward(width)
t.right(90)
t.forward(length)
t.right(90)
