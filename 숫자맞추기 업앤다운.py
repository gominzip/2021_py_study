#숫자 맞추기 업다운 게임

import random  #랜덤 함수 사용을 위한 설정
com_num = random.randint(1,100)

user_num = int(input('제가 생각한 숫자를 맞춰보세요!: '))

시도횟수= 1

while user_num != com_num :
    if user_num >= com_num :
        print("%d 보다 더 작은 수를 입력하세요. Down Down!" % user_num)
    elif user_num <= com_num :
        print("%d 보다 더 큰 수를 입력하세요. Up Up!" % user_num)
    user_num=int(input('숫자를 다시 입력하세요: '))
    시도횟수= 시도횟수+1

print('%d ! 정답입니다! %d회 시도하여 맞췄습니다.' %(com_num,시도횟수))
