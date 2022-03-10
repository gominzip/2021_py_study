scores=[85, 70, 90, 98, 87, 68, 77, 100, 75, 80] #0~9

n=0

for i in range(0,10,1):
    n= n + scores[i]

average=n/10

print('학생 10명의 점수 평균은 %.2f 입니다.' %average)
