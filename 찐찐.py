import random
win=0
lose=0

while win<4 or lose<4 :
    com = random.randint(1.3)
    user = int(input('가위바위보를 선택하세요 (1.가위, 2.바위, 3.보)'))
    if user==1:
        a='가위'
    elif user==2:
        a='바위'
    elif user==3:
        a='보'
        
    if com==1:
        b='가위'
    elif com==2:
        b='바위'
    elif com==3:
        b='보'
        
    print('======================================================')
    print('당신의 선택은 (%s)입니다.' %a)
    print('컴퓨터의 선택은 (%s)입니다.' %b)

    if user == com :
        print('비겼습니다. 현재 스코어 %d승 %d패' %(win, lose))
    elif user - com == 1 or (user==1 and com==3) :
        win=win+1
        print('이겼습니다! 현재 스코어 %d승 %d패' %(win, lose))
    else:
        lose=lose+1
        print('졌습니다!  현재 스코어 %d승 %d패' %(win, lose))
    user = int(input('가위바위보를 선택하세요 (1.가위, 2.바위, 3.보) :'))
