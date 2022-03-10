import csv

data=[]
with open('sample.csv', 'r') as f:
    csv_data = csv.reader(f)
    print(type(csv_data))
    header = next(csv_data)
    for row in csv_data:
        data.append(row)

print(header)
print(data)
