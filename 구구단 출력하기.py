#구구단 출력하기
num=1
a=int(input('몇 단을 출력할까요? '))

while num < 10 :
    print('%d * %d =%d' % (a,num,a*num))
    num=num+1
    
