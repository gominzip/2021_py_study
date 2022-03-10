numbers=[]

for i in range(1,10002,1):
    if ('3'in str(i)) or ('6'in str(i)) or ('9' in str(i)):
        numbers.append('*')
    else:
        numbers.append(i)
    
with open('369.txt','w') as f:
    for n in range(10001):
        f.write('%s' %numbers[n])

f.close()
