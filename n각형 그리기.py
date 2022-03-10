#n-각형 그리기
num=int(input('몇각형을 그릴까요?: '))

import turtle
t = turtle.Pen()
angle = 360/num

for i in range(num):
    t.forward(100)
    t.right(angle)
