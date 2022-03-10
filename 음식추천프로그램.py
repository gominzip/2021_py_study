import random

한식=['불고기', '제육볶음', '닭볶음탕', '김치찌개']
중식=['짜장면', '짬뽕', '마라탕', '훠궈']
일식=['스키야키', '우동', '스시', '돈카츠']
양식=['파스타', '피자', '치킨', '스테이크']

print('어떤 음식 종류를 추천할까요?')
print('한식(1) 중식(2) 일식(3) 양식(4) 아무거나(5)')
num=int(input('입력 : '))

if num==5:
    num=random.randint(1,4)

if num==1 :
    print('오늘의 추천음식 : %s' %한식[random.randint(0,3)])
elif num==2 :
    print('오늘의 추천음식 : %s' %중식[random.randint(0,3)])
elif num==3 :
    print('오늘의 추천음식 : %s' %일식[random.randint(0,3)])
elif num==4 :
    print('오늘의 추천음식 : %s' %양식[random.randint(0,3)])
