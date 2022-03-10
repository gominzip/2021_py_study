#사칙연산 계산기
num1=float(input('첫 번째 값을 입력하세요 :'))
symbol=input('연산 기호를 입력하세요(+,-,*,/) :')
num2=float(input('두 번째 값을 입력하세요 :'))

if symbol=='+':
    a=num1+num2
elif symbol=='-':
    a=num1-num2
elif symbol=='*':
    a=num1*num2
else :
    a=num1/num2

print('=============================================')
print(num1, symbol, num2,'=', a)
