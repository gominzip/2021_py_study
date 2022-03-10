import csv
with open('NHIS_OPEN_T20_2016.csv', 'r') as f:
    csv_data = csv.reader(f)
    next(csv_data)
    count=0
    totalday=0
    for row in csv_data:
        sido = int(row[5])
        medical = int(row[8])
        form = int(row[7])
        days = int(row[12])
        if sido==26 and medical==1 and form==2:
            count=count+1
            totalday=totalday + days
            
print(count)
print('평균 입내원일 수 : %.2f days' %(totalday/count))

