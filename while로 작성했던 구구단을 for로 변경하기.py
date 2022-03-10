#while로 작성했던 구구단을 for로 변경하기

dan= int(input('몇 단을 출력할까요? : '))

for i in range(1,10,1):
    print('%d * %d = %d' %(dan,i,dan*i))
