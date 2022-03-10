#산술연산자
ap=2000
lp=3000
cp=3500

ame=int(input('아메리카노 판매수: '))
latte=int(input('카페라떼 판매수: '))
capu=int(input('카푸치노 판매수: '))
money=ame*ap+latte*lp+capu*cp

print('총 매출은 %d원 입니다.' %money)
