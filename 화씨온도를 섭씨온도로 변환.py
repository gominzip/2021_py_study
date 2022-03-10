#회씨 온도를 섭씨로 변환
F=int(input('(정수만)화씨온도: '))
C=(F-32)*5/9
print('섭씨온도: %f' %C)

#int를 이용하면 정수만 가능, 소수점도 계산하려면 float
F=float(input('화씨온도: '))
C=(F-32)*5/9
print('섭씨온도: %f' %C)
