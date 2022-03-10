#수학함수이용_두점사이의 거리 구하기
x1=float(input('첫번째 점의 x값을 입력하세요 : '))
y1=float(input('첫번째 점의 y값을 입력하세요 : '))
x2=float(input('두번째 점의 x값을 입력하세요 : '))
y2=float(input('두번째 점의 y값을 입력하세요 : '))

#제곱근 안에 들어갈 값 계산 (거리공식참고)
bb=(x1-x2)**2 + (y1-y2)**2

#수학함수제곱급(sqrt)이용
import math
a = math.sqrt(bb)

#출력
print('두 점 (%d,%d)와 (%d,%d) 사이의 거리는 %f 입니다.' % (x1,y1,x2,y2,a))
