def isPrimeNumber(n):
    if n<2:
        return False
    for i in range(2,n,1):
        if n%i == 0:
            return False
    return True

num= int(input('숫자를 입력하세요:'))
count=0
for n in range(num+1):
    if isPrimeNumber(n)==True:
        count=count+1
        print(n)

print('%d이하의 숫자 중 소수는 %d개가 존재합니다.'%(num, count))
