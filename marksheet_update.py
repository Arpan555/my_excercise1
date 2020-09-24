students = [
    {'sno': 22, 'name': 'fd', 'last_name': 'dd', 'clas': '5', 'section': 'd', 
        'subjects': [{'subject': 'hindi', 'total_marks': '300', 'marks': '200'}, 
                    {'subject': 'math', 'total_marks': '500', 'marks': '200'}, 
                    {'subject': 'sancrit', 'total_marks': '300', 'marks': '100'}
                    ]
    }, 
    {'sno': 23, 'name': 'kapil', 'last_name': 'sharma', 'clas': '2', 'section': 'c', 
        'subjects': [
            {'subject': 'hindi', 'total_marks': '100', 'marks': '10'}, 
            {'subject': 'math', 'total_marks': '100', 'marks': '20'}
        ]
        }
    ]
 
def add_student():
    data = {}
    sno = int(input("Enter S.No: "))
    name = input("Enter Student Name: ")
    last_name = input("Enter Last name: ")
    clas = input("Enter Class: ")
    section = input("Enter Section: ")
    data["sno"]=sno
    data["name"]=name
    data["last_name"]=last_name
    data["clas"]=clas
    data["section"]=section
    students.append(data)
    return sno
    
 
def add_subjects(sno):
    input_val = int(input("Enter 11 for add subject and enter 22 for main menu"))
    if input_val == 11: 
        subject = input("Enter Subject Name:")
        total_marks = input("Total Marks of Subject:")
        marks = input("Marks:")
        sub = {'subject':subject,'total_marks':total_marks,'marks':marks}
        for student in students:
            if student['sno'] is sno :
                if student.get('subjects'):
                    subjects = student['subjects']
                    subjects.append(sub)
                else:
                    student['subjects'] = [sub]
        add_subjects(sno)
    elif input_val == 22:
        return False
    else:
        return None
 
 
def update_student(sno):
    for student in students:
        if student['sno'] is sno :
            name = input("Enter Student Name: ")
            last_name = input("Enter Last name: ")
            clas = input("Enter Class: ")
            section = input("Enter Section: ")
            student["name"]=name
            student["last_name"]=last_name
            student["clas"]=clas
            student["section"]=section
            print ("Stundent updated!!")
            return True
    return False
 
 
def update_subject(sno):
    input_val =input("Enter sub for update  or 22 for exit")
    if input_val == '22':
        return False
    total_marks = input("Total Marks of Subject:")
    marks = input("Marks:")
    for student in students:
        if student['sno'] is sno :
            if student.get('subjects'):
                subjects = student['subjects']
                for subject in subjects:
                    if subject['subject'] == input_val:
                        subject['total_marks'] = total_marks
                        subject['marks'] = marks
                    else :
                        print ("Given subject Not exist")
 
    update_subject(sno)
 
 
def show_student(sno):
    for student in students:
        if student['sno'] is sno :
            print (student)
            show(student)
 
def show(student):
    s = " "
    d = "-"
    print(f"\n\n|{ d * 30 } CENTRAL BOARD OF SECONDAY EDUCATION { d * 30 }|\n|{ s * 41 }MARKS STATEMENT{ s * 41 }|\n|{ s * 32 }SECONDAY SCHOOL EXAMINATION, 2020{ s * 32 }|")
    print(f"|{ s * 97 }|\n|{ s * 97 }|")
    print(f"|{ s * 10 }Name          : {student['name']} { s * 71 }|\n|{ s * 10 }Fathers Name  : {student['clas']}{ s * 30 }Roll.No :{ s * 32 }|\n|{ s * 10 }Mothers Name  : { s * 71 }|\n|{ s * 10 }Date of Birth : { s * 71 }|\n|{ s * 10 }School        : { s * 71 }|\n|{ s * 97 }|\n|  |{ d * 8 }|{ d * 24 }|{ d * 44 }|{ d * 12 }|{ s * 2 }|")
    print(f"|  |{ s * 8 }|{ s * 24 }|{ s * 20 }MARKS{ s * 19 }|{ s * 12 }|{ s * 2 }|\n|{ s * 2 }|  SUB   |{s * 8 }SUBJECT{ s * 9 }|{ d * 44 }| POSITIONAL |{ s  * 2 }|\n|{ s  * 2 }|  CODE  |{ s  * 24 }|  TOTAL  |  OBTAINED  |{ s  * 6 }IN WORDS{ s  * 7 }|    GRADE   |{ s  * 2 }|\n|  |{ d * 8 }|{ d * 24 }|{ d * 9 }|{ d * 12 }|{ d * 21 }|{ d * 12 }|{ s * 2 }|\n|  |{ s * 8 }|{ s * 24 }|{ s * 9 }|{ s * 12 }|{ s * 21 }|{ s * 12 }|{ s * 2 }|\n|  |{ s * 8 }|{ s * 24 }|{ s * 9 }|{ s * 12 }|{ s * 21 }|{ s * 12 }|{ s * 2 }|\n|  |{ s * 8 }|{ s * 24 }|{ s * 9 }|{ s * 12 }|{ s * 21 }|{ s * 12 }|{ s * 2 }|")
    print(f"|  |{ d * 8 }|{ d * 24 }|{ d * 9 }|{ d * 12 }|{ d * 21 }|{ d * 12 }|{ s * 2 }|\n|{ s * 97 }|\n|{ s * 97 }|\n|{ s * 34 }Result :{ s * 55 }|\n|{ s * 97 }|\n|{ d * 97 }|")
 
 
x = True
while x == True:
    ch1 = int(input("Enter choice: \n 1. Add new record of student \n 2. Update the record \n 3. Display the record \n   4. Update the subject \n 5. Exit \n"))
    if ch1 == 1:
        sno = add_student()
        add_subjects(sno)
        print (students)
 
    elif ch1 == 2:
        sno = int(input("Enter S.No: "))
        if not  update_student(sno):
            print ("Wrong S.No.")
    elif ch1 == 3:
        sno = int(input("Enter S.No: "))
        show_student(sno)
    elif ch1 == 4:
        sno = int(input("Enter S.No: "))
        update_subject(sno)
    elif ch1 == 5:
        break
