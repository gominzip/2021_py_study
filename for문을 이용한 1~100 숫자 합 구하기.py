#for문을 이용한 1~100 숫자 합 구하기

num=0
hol=0
zzak=0
for i in range(1,101,1):
    num=num+i  #num += i도 가능 (i만큼더한다)

for i in range(1,101,2):    #새로 num=0으로해도 ㄱㅊ
    hol=hol+i

for i in range(2,101,2):
    zzak=zzak+i
    
print('1부터 100까지의 합은 %d입니다.' %num)
print('1부터 100까지의 홀수의 합은 %d입니다.' %hol)
print('1부터 100까지의 짝수의 합은 %d입니다.' %zzak)


#사용자가 입력한 값 까지의 합계 출력

user= int(input('1부터 몇 까지의 합을 구할까요?:'))
num=0
for i in range(1,user+1,1):
    num+=i

print('1부터 %d까지의 합은 %d입니다.' %(user,num))
