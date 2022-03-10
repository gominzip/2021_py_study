#제주에서의 진료내역 csv로 저장
import csv
jeju_data = []
with open('NHIS_OPEN_T20_2016.csv', 'r') as f:
    csv_data = csv.reader(f)
    header=next(csv_data)
    for row in csv_data:
        sido=int(row[5])
        if sido==49:
            jeju_data.append(row)

with open('JEJU_HISTORY.csv', 'w', newline='') as f:
    wr=csv.writer(f)
    wr.writerow(header) #헤더도 추가
    for row in jeju_data:
        wr.writerow(row)
