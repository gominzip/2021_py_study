n=1500
count=0
for i in range(n+1):
    result=True
    if(i<2):
        result=False
    for j in range(2,i):
        if(i%j==0):
            result=False
    if result:
        count=count+1
        print(i, end=' ')

print('\n',count)

