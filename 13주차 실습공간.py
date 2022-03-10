#13주차 실습공간_처방일수구하기
import csv
with open('NHIS_OPEN_T20_2016.csv', 'r') as f:
    csv_data = csv.reader(f)
    next(csv_data)
    count=0
    totalday=0
    for row in csv_data:
        sex = int(row[3]) #데이터가 숫자여도 int로 숫자인 걸 알려주고 변환
        age = int(row[4])
        sido = int(row[5])
        medical = int(row[8])
        day = int(row[17])
        if age==11 or age==12:
            if sex==2 and sido==28 and medical==12:
                print('처방일 수 : %s' %day)
                count=count+1
                totalday=totalday + day

print('평균 처방일 수 : %.2f days' %(totalday/count))

