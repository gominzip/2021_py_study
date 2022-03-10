#파이썬 거북이 사용을 위한 초기 설정
import turtle
t = turtle.Pen()
t.shape('turtle')
t.speed(0)

#거북이로 그림그리기
length = 1               #변수 생성하고 1저장

while length < 500:    #while 반복문 사용, length 변수값이 500 미만인 동안 반복
    t.forward(length)   #length만큼 선그리기     
    t.right(90)        #90도 회전하기
    length = length + 1 #변수값 증가 
