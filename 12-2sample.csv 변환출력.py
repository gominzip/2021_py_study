#12-2sample.csv 변환출력
import csv

data=[]
with open('sample.csv','r') as f:
    csv_data = csv.reader(f)
    header = next(csv_data)

    for row in csv_data:
        data.append(row)


for row in data:
    age = 2021 - int(row[3])+1
    print('이름 : %s\t키 : %s\t몸무게 : %s\t나이 : %s\t혈액형 : %s' %(row[0],row[1],row[2],age,row[4]))
