#입력 문자에서 글자 수 세기

문장=input('문장을 입력하세요:')
글자=input('어떤 글자를 찾을까요?:')

count=0

for i in 문장:
    if i == 글자:
        count+=1

print('입력한 문장에서 %s의 갯수는 %d개 입니다.' %(글자,count))
