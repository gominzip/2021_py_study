#자동 판매기 프로그램
pay=int(input('투입한 돈: '))
price=int(input('물건값: '))
거스름돈=pay-price
오백원=거스름돈//500
백원=(거스름돈%500)//100
print('거스름돈: %d' %거스름돈)
print('500원 동전의 개수: %d' %오백원)
print('100원 동전의 개수: %d' %백원)
