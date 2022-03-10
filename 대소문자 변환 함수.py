#대소문자 변환 함수
def change_case(text):

    result = ""

    for c in text:  #for문으로 한글자 한글자 탐색해 c에 담기
        if c.isupper() == True:
            result = result + c.lower()
        elif c.islower() == True:
            result = result + c.upper()
        else:
            result= result + c


    return result


text = input('문자열을 입력하세요:')
print('%s를 %s로 변환하였습니다.' %(text, change_case(text)) )
