#초를입력받고 시간분초로 환산
num=int(input('초단위 시간을 입력하세요: '))

#환산하기
hour=num//3600
minute=(num%3600)//60
second=num%60

#출력
print('%d초는 환산하면 %d시간 %d분 %d초입니다.' %(num,hour,minute,second))
 
