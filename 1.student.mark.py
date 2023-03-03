import json

students_list = []
course_list = []
students_list_in_use = []
num_students = 0

#get student info
def student_info(num_of_students):
    for i in range(0, num_of_students):
        student_dict = {}
        student_id = input("\nEnter Student " + str(i+1) +" ID: ")
        student_name = input("Enter student " + str(i+1) +" 's name: ")
        student_dob = input("Enter student " + str(i+1) +" 's date of birth: ")
        student_dict['ID: '] = student_id
        student_dict['Name: '] = student_name
        student_dict['Date of birth: '] = student_dob
        students_list.append(student_dict)
        
#get course info
def course_info(num_of_course):
    for i in range(0, num_of_course):
        course_dict = {}
        course_id = input("\nEnter Course " + str(i+1) +" ID: ")
        course_name = input("Enter Course " + str(i+1) +" 's name: ")
        course_dict['ID: '] = course_id             
        course_dict['Name: '] = course_name
        course_list.append(course_dict)             

#remove student from list
def Remove_Student_From_List():
    print("List of student: ")
    for i in range(0, len(students_list)):
        print(students_list[i]['ID: '])
    student_id = input("Enter student ID you want to remove: ")
    for i in range(0, len(students_list)):
        if students_list[i]['ID: '] == student_id:
            students_list.remove(students_list[i])
            print("Student has been removed\n")
            break
        else:
            print("Student not found\n")
    print(json.dumps(students_list, indent = 4))

#add student to course
def Add_Students_to_Course(student_list, course):
    print("List of student:")
    for i in range(0, len(student_list)):
        print(student_list[i]['ID: '])   
    student_id = input("Enter student ID: ")
    student_id = student_id.split()
    student_id.sort()
    for i in range(0, len(course_list)):
        if course_list[i]['ID: '] == course:
            if 'Student: ' in course_list[i]:
                course_list[i]['Student: '].append(student_id)
            else:
                course_list[i]['Student: '] = [student_id]
            print("Student has been added\n")

#add mark for student
def insert_mark_to_student():
    print("Course available: ")
    for i in range(0, len(course_list)):
        print(course_list[i])
    course = input("Enter course ID: ")
    print("List of student:")
    for i in range(0, len(course_list)):
        if course_list[i]['ID: '] == course:
            for j in range(0, len(course_list[i]['Student: '])):
                print(course_list[i]['Student: '][j])
                print("\n")
    count = 0
    for i in range(0, len(course_list)):
        if course_list[i]['ID: '] == course:
            count += 1
            for j in range(0, len(course_list[i]['Student: '])):
                for k in range(0, len(course_list[i]['Student: '][j])):
                    print("Student ID: " + course_list[i]['Student: '][j][k])
                    mark = (input("Enter student mark: "))
                    if 'Mark: ' in course_list[i]:
                        course_list[i]['Mark: '].append(mark)
                    else:
                        course_list[i]['Mark: '] = [mark]
                    print("Mark has been added\n")
    if count == 0:
        print("Student not found\n")

#display student list
def display_mark_table():
    print("Course available: ")
    for i in range(0, len(course_list)):
        if 'Student: ' in course_list[i]:
            print(course_list[i])
    course = input("Enter course ID: ")
    print("ID\tName\tMark")
    count = 0
    for i in range(0, len(course_list)):
        if course_list[i]['ID: '] == course:
            for j in range(0, len(course_list[i]['Student: '])):
                for k in range(0, len(course_list[i]['Student: '][j])):
                    for l in range(0, len(students_list)):
                        if course_list[i]['Student: '][j][k] == students_list[l]['ID: ']:
                            count += 1
                            print(course_list[i]['Student: '][j][k] + "\t" + students_list[l]['Name: ']+ "\t" + course_list[i]['Mark: '][k])
                    if count == 0:
                        print("Student not found")
                        break
            if 'Student: ' not in course_list[i]:
                print("Course is empty")

#main
while (1):
    print("\nChoose option: ")
    print("1. Add student")
    print("2. Remove student")
    print("3. Add course")
    print("4. Add student to course")
    print("5. Add mark for student")
    print("6. Display Student list")
    print("7. Display Course list")
    print("8. Display Mark list ")
    print("9. Exit\n")
    option = int(input("Enter option:  "))
    if option == 1:
        num_of_student = int(input("\nEnter number of student: "))
        student_info(num_of_student)
        students_list_in_use = students_list
        students_list.sort(key = lambda i: i['ID: '])   
        print(json.dumps(students_list, indent = 4))    
    elif option == 2:                                   
        Remove_Student_From_List()
    elif option == 3:
        num_of_course = int(input("\nEnter number of course: "))
        course_info(num_of_course)
        course_list.sort(key = lambda i: i['ID: '])     
        print(json.dumps(course_list, indent = 4))
    elif option == 4:                                   
        print("\nList of course:")
        for i in range(0, len(course_list)):
            print(course_list[i]['ID: '])
        course = input("\nEnter course ID: ")
        Add_Students_to_Course(students_list, course)        
    elif option == 5:                                  
        insert_mark_to_student()
    elif option == 6:                                                 
        print(json.dumps(students_list, indent = 4))
    elif option == 7:                                  
        print(json.dumps(course_list, indent = 4))
    elif option == 8: 
        display_mark_table()
    elif option == 9:                                  
        break
    else:
        print("\nInvalid option\n")
