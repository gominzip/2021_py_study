with open('새파일.txt', 'r') as f:
    data = f.readlines()
    print(data)

for line in data:
    print(line)
