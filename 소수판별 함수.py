#소수판별 함수

def isPrimeNumber(number):
    if number<2:
        return False
    
    for n in range(2, number, 1):
        if number%n == 0:
            return False

    return True #else에 대해 리턴 트루x


number = int(input('숫자를 입력하세요: '))

if isPrimeNumber(number)==True:
    print('%d는 prime number 입니다' %number)
else:
    print('%d는 prime number가 아닙니다' %number)


#개선 코드(시간단축을 위해 짝수 제외)
import time

def isPrimeNumber(number):
    시작시간 = time.time()
    if number<2:
        return False

    if number==2:
        return True

    if number%2 ==0:
        return False
    
    for n in range(2, number, 1):
        if number%n == 0:
            return False
    print('걸린시간 : ', (time.time() - 시작시간))

    return True #else에 대해 리턴 트루x


number = int(input('숫자를 입력하세요: '))

if isPrimeNumber(number)==True:
    print('%d는 prime number 입니다' %number)
else:
    print('%d는 prime number가 아닙니다' %number)
