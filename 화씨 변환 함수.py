#화씨 변환 함수

def CtoF(c):
    F= (c*1.8)+32
    return F

c= int(input('섭씨 온도를 입력하세요:'))
f= CtoF(c)

print('섭씨 %d도는 화씨 %.1f도 입니다.' %(c,f))
