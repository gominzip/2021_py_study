#for문 중첩 구구단 2단부터 9단까지 전체 출력하기

for i in range(2,10,1):  #구구단 증가시키기
    for num in range(1,10,1):    #한 단내에서 곱할 수를 증가시키는 반복
        print("%d * %d = %d" %(i,num,i*num))
    print("================")
