student_list=[]
student_list.append({'학번':1000, '이름':'홍길동', '학과':'열공학과'})
student_list.append({'학번':1001, '이름':'강감찬', '학과':'경영학과'})
student_list.append({'학번':1002, '이름':'이순신', '학과':'물리학과'})
student_list.append({'학번':1003, '이름':'신사임당', '학과':'열공학과'})

print('==모든 학생의 정보 출력==')

for i in range(0, len(student_list),1): #1en()-리스트내의 데이터 개수세기
    print('학번 : %d, 이름 : %s' %(student_list[i]['학번'], student_list[i]['이름']))

    
print('')
print('==열공학과 학생 이름 출력==')
for i in range(0, len(student_list),1):
    if student_list[i]['학과']=='열공학과':
        print(student_list[i]['이름'])
        
print('')

#쉬운 버전, 인덱스 렌지 사용x
for student in student_list:
    print('학번 : %d, 이름 : %s' %(student['학번'], student['이름']))

print('')
print('==열공학과 학생 이름 출력==')
for student in student_list:
    if student['학과']=="열공학과":
        print(student['이름'])

#학과도 검색해서
print('')
질문=input('어떤 학과를 검색할까요?:')
for student in student_list:
    if student['학과']==질문:
        print(student['이름'])
