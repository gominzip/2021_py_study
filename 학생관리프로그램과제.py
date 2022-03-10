student_list = []
student_list.append({"학번":1000, "이름":"홍길동", "학과":"열공학과"})
student_list.append({"학번":1001, "이름":"강감찬", "학과":"체육학과"})
student_list.append({"학번":1002, "이름":"이순신", "학과":"물리학과"})
student_list.append({"학번":1003, "이름":"신사임당", "학과":"열공학과"})

while True :
    end=0
    print("┌------------------------------------------------┐")
    print("│ 학생관리 프로그램 V 1.0 created by 고민지      │")
    print("├------------------------------------------------┤")
    print("│1.전체출력  2.검색  3.신규 학생추가      0.종료 │")  
    print("└------------------------------------------------┘")
    number = int(input("명령을 입력해주세요 : "))


    while True :
        if number==1 :  
            print()
            print("┌------------------------------------------------┐")
            print("│ 전체 학생 목록                                 │")
            print("└------------------------------------------------┘")
            for student in student_list:
                print('학번 : %d, 이름 : %s, 학과 : %s' % (student['학번'], student['이름'], student['학과']))
            break
                

        elif number==2 :
             print()
             print("┌------------------------------------------------┐")
             print("│ 검색 종류를 선택하세요.                        │")
             print("├------------------------------------------------┤")
             print("│1.이름검색   2.학과검색                         │")
             print("└------------------------------------------------┘")
             search = int(input('검색 메뉴를 선택하세요 :'))


             while True:
                 if search==1 :
                     name=input('검색할 이름을 입력하세요 : ')
                     n=0
                     for student in student_list:
                         if name in student['이름']:
                             print('학번 : %d, 이름 : %s, 학과 : %s' % (student['학번'], student['이름'], student['학과']))
                         else :
                             n=n+1
                             if n==len(student_list):
                                 print('검색 결과가 없습니다.')
                     break

                     
                 elif search==2 :
                     major=input('검색할 학과를 입력하세요 : ')
                     n=0
                     for student in student_list:
                         if major in student['학과']:
                             print('학번 : %d, 이름 : %s, 학과 : %s' % (student['학번'], student['이름'], student['학과']))
                         else :
                              n=n+1
                              if n==len(student_list):
                                 print('검색 결과가 없습니다.')
                     break
                 
                 else:
                     search = int(input('잘못된 검색 명령입니다. 다시 입력해주세요 : '))
                    
             break
                     



        elif number==3 :
            print('신규 학생 정보를 등록합니다.')
            newnum=int(input('학번을 입력하세요 : '))
            newname=input('이름을 입력하세요 : ')
            newmajor=input('학과를 입력하세요 : ')
            student_list.append({"학번": newnum, "이름": newname, "학과": newmajor })
            print('신규학생이 추가되었습니다.')
            break



            
        elif number==0 :
            print()
            print("┌------------------------------------------------┐")
            print("│ 프로그램을 종료합니다.                         │")
            print("└------------------------------------------------┘")
            end=1
            break


            
        else :
            number=int(input('잘못된 명령입니다. 명령을 입력해주세요 : '))


    if end==1:
        break
    
    print()
    print("==출력 종료==")
    input("계속하려면 엔터키를 누르세요…")
    


