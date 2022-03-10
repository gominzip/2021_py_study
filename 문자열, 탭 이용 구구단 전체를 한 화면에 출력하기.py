#문자열, 탭 이용 구구단 전체를 한 화면에 출력하기

for second in range(1,10,1):
    sentence=""  #처음 시작줄 출력할 내용 비움
    for first in range(2,10,1):
        sentence = sentence + "%d X %d = %d \t" % (first, second, first*second)
    print(sentence) #second, 즉 가로줄 하나씩 프린트

print("==========================================================")
#한번에 프린트하기
sen=""
for num in range(1,10,1):
    for dan in range(2,10,1):
        sen = sen + "%d X %d = %d \t" % (dan,num,dan*num)
    sen=sen+"\n"

print(sen)
