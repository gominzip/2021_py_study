#bmi계산결과 파일로 내보내기
import csv
data=[]
result=[]
with open('sample.csv','r') as f:  #sample.csv데이터 리스트로 옮기기
    csv_data = csv.reader(f)
    header = next(csv_data)
    for row in csv_data:
        data.append(row)


for row in data:
    height=int(row[1])/100
    weight=int(row[2])
    BMI = weight/(height**2)
    if BMI<18.5 :
        con='저체중'
    elif BMI<25 :
        con='정상체중'
    elif BMI<30 :
        con='과체중'
    elif BMI<35 :
        con='비만'
    elif BMI<40 :
        con='고도비만'
    else :
        con='초고도비만'
    result.append([row[0], BMI, con])  #result 리스트에 데이터 추가

with open('result.csv', 'w', newline='')as f:   #result.csv에 result 데이터 추가
    wr = csv.writer(f)
    for row in result:
        wr.writerow(row)
