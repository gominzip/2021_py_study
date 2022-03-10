#시험점수에 대한 학점 출력하기
a=int(input('성적을 입력하시오: '))

if a>=90 :
    print('A학점 입니다.')
else :
    if a>=80 :
        print('B학점 입니다.')
    else :
        if a>=70 :
            print('C학점 입니다.')
        else :
            if a>=60 :
                print('D학점 입니다.')
            else :
                print('F학점 입니다.')
