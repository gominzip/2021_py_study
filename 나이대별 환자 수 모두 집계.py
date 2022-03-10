#나이대별 환자 수 모두 집계
import csv
ages = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
with open('NHIS_OPEN_T20_2016.csv', 'r') as f:
    csv_data = csv.reader(f)
    next(csv_data)
    for row in csv_data:
        age=int(row[4])
        ages[age-1]=ages[age-1]+1

            
for i in range(len(ages)):
    print('Age %d ~ %d : %d' %(i*5, i*5+4, ages[i]))
