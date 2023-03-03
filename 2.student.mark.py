import json

class get_info:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return f"ID: {self.id}  Name: {self.name}"


class Student(get_info):
    student_list = []

    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.dob = dob
    
    def insert_info(id, name, dob):
        student_dict = {}
        student_dict['ID: '] = id
        student_dict['Name: '] = name
        student_dict['Date of birth: '] = dob
        Student.student_list.append(student_dict)
        Student.student_list = sorted(Student.student_list, key=lambda i: i['ID: '])

    def __str__(self):
        return super(Student, self).__str__() + f"  Date of birth: {self.dob}"

    def display_student():
        Student.student_list = sorted(Student.student_list, key=lambda i: i['ID: '])
        print("ID\t\tName\t\tDate of birth")
        for i in range(0, len(Student.student_list)):
            print(Student.student_list[i]['ID: '], end="\t\t")
            print(Student.student_list[i]['Name: '], end="\t\t")
            print(Student.student_list[i]['Date of birth: '])
    
    def modify_student_info():
        print("List of student\n:")
        print("ID\t\tName\t\tDate of birth")
        for i in range(0, len(Student.student_list)):
            print(Student.student_list[i]['ID: '], end="\t\t")
            print(Student.student_list[i]['Name: '], end="\t\t")
            print(Student.student_list[i]['Date of birth: '])
        options = int(input("Enter 1 to modify student ID, 2 to modify student name, 3 to modify student date of birth, 4 to remove completely: "))
        if options == 1:
            count1 = 0
            student_id = input("Enter student ID you want to modify: ")
            for i in range(0, len(Student.student_list)):
                if Student.student_list[i]['ID: '] == student_id:
                    count1 += 1
                    new_id = input("Enter new ID: ")
                    Student.student_list[i]['ID: '] = new_id
                    print("Student ID has been modified\n")
                    break
            if count1 == 0:
                print("Student not found\n")
        elif options == 2:
            count2 = 0
            student_id = input("Enter student ID you want to modify: ")
            for i in range(0, len(Student.student_list)):
                if Student.student_list[i]['ID: '] == student_id:
                    count2 += 1
                    new_name = input("Enter new name: ")
                    Student.student_list[i]['Name: '] = new_name
                    print("Student name has been modified\n")
                    break
            if count2 == 0:
                print("Student not found\n")
        elif options == 3:
            count3 = 0
            student_id = input("Enter student ID you want to modify: ")
            for i in range(0, len(Student.student_list)):
                if Student.student_list[i]['ID: '] == student_id:
                    count3 += 1
                    new_dob = input("Enter new date of birth: ")
                    Student.student_list[i]['Date of birth: '] = new_dob
                    print("Student date of birth has been modified\n")
                    break
            if count3 == 0:
                print("Student not found\n")
        elif options == 4:
            count4 = 0
            student_id = input("Enter student ID you want to remove: ")
            for i in range(0, len(Student.student_list)):
                if Student.student_list[i]['ID: '] == student_id:
                    count4 += 1
                    Student.student_list.remove(Student.student_list[i])
                    print("Student has been removed\n")
                    break
            if count4 == 0:
                print("Student not found\n")
    
class Course(get_info):
    course_list = []
    
    def __init__(self, id, name):
        super().__init__(id, name)

    def insert_info(id, name):
        course_dict = {}
        course_dict['ID: '] = id
        course_dict['Name: '] = name
        Course.course_list.append(course_dict)

    def __str__(self):
        return super(Course, self).__str__()

    def display_course():
        Course.course_list = sorted(Course.course_list, key=lambda i: i['ID: '])
        print(json.dumps(Course.course_list, indent=4))

    def remove_course():
        print("List of course:")
        for i in range(0, len(Course.course_list)):
            print(Course.course_list[i]['ID: '])
        course_id = input("Enter course ID you want to remove: ")
        for i in range(0, len(Course.course_list)):
            if Course.course_list[i]['ID: '] == course_id:
                Course.course_list.remove(Course.course_list[i])
                print("Course has been removed\n")
                break
            else:
                print("Course not found\n")
        print(Course.course_list)

class Student_Management(Student, Course):
    def add_student_to_course():
        print("Course available: ")
        for i in range(0, len(Course.course_list)):
            print(Course.course_list[i])
        course = input("Enter course ID: ")
        Student.student_list = sorted(Student.student_list, key=lambda i: i['ID: '])
        print("List of student:")
        for i in range(0, len(Student.student_list)):
            print(Student.student_list[i]['ID: '])   
        student_id = input("Enter student ID: ")
        student_id = student_id.split()
        student_id.sort()
        print(student_id)
        count = 0
        count_st = 0
        for i in range(0, len(Course.course_list)):
            if Course.course_list[i]['ID: '] == course:
                count += 1
                for j in range(0, len(student_id)):
                    for k in range(0, len(Student.student_list)):
                        if student_id[j] == Student.student_list[k]['ID: ']:
                            count_st += 1
                            break
                if count_st != 0:
                    if 'Student :' in Course.course_list[i]:
                        Course.course_list[i]['Student: '].append(student_id)
                    else:
                        Course.course_list[i]['Student: '] = [student_id]
                    print("Student has been added\n")
        if count == 0:
            print("Course not found\n")
        print(json.dumps(Course.course_list, indent=4))
    
    def remove_student_from_course():
        print("Course available: ")
        for i in range(0, len(Course.course_list)):
            print(Course.course_list[i])
        course = input("Enter course ID: ")
        print("List of student:")
        for i in range(0, len(Student.student_list)):
            print(Student.student_list[i]['ID: '])
        student_id = input("Enter student ID you want to remove: ")
        student_id = student_id.split()
        student_id.sort()
        count = 0
        for i in range(0, len(Course.course_list)):
            if Course.course_list[i]['ID: '] == course:
                count += 1
                if 'Student :' in Course.course_list[i]:
                    Course.course_list[i]['Student: '].remove(student_id)
                    print("Student has been removed\n")
                    break
        if count == 0:
                print("Student not found\n")
        print(json.dumps(Course.course_list, indent=4))
    
    def insert_mark_to_student():
        print("Course available: ")
        for i in range(0, len(Course.course_list)):
            print(Course.course_list[i])
        course = input("Enter course ID: ")
        print("List of student:")
        for i in range(0, len(Course.course_list)):
            if Course.course_list[i]['ID: '] == course:
                for j in range(0, len(Course.course_list[i]['Student: '])):
                    print(Course.course_list[i]['Student: '][j])
                    print("\n")
        count = 0
        for i in range(0, len(Course.course_list)):
            if Course.course_list[i]['ID: '] == course:
                count += 1
                for j in range(0, len(Course.course_list[i]['Student: '])):
                    for k in range(0, len(Course.course_list[i]['Student: '][j])):
                        print("Student ID: " + Course.course_list[i]['Student: '][j][k])
                        mark = (input("Enter student mark: "))
                        if 'Mark: ' in Course.course_list[i]:
                            Course.course_list[i]['Mark: '].append(mark)
                        else:
                            Course.course_list[i]['Mark: '] = [mark]
                        print("Mark has been added\n")
        if count == 0:
            print("Student not found\n")
        
    def display_mark_table():
        print("Course available: ")
        for i in range(0, len(Course.course_list)):
            if 'Student: ' in Course.course_list[i]:
                print(Course.course_list[i])
        course = input("Enter course ID: ")
        print("ID\tName\tMark")
        count = 0
        for m in range(0, len(Course.course_list[m])):
            if 'Mark: ' not in Course.course_list[m]:
                print("Students don't have mark")
                break
            else:
                for i in range(0, len(Course.course_list)):
                    if Course.course_list[i]['ID: '] == course:
                        for j in range(0, len(Course.course_list[i]['Student: '])):
                            for k in range(0, len(Course.course_list[i]['Student: '][j])):
                                for l in range(0, len(Student.student_list)):
                                    if Course.course_list[i]['Student: '][j][k] == Student.student_list[l]['ID: ']:
                                        count += 1
                                        print(Course.course_list[i]['Student: '][j][k] + "\t" + Student.student_list[l]['Name: ']+ "\t" + Course.course_list[i]['Mark: '][k])
                                if count == 0:
                                    print("Student not found")
                                    break
                        if 'Student: ' not in Course.course_list[i]:
                            print("Course is empty")


    def main():
        print("\n1. Add student")
        print("2. Remove student")
        print("3. Add course")
        print("4. Remove course")
        print("5. Add student to course")
        print("6. Remove student from course")
        print("7. Insert mark to student")
        print("8. Display student list")
        print("9. Display course list")
        print("10. Display table mark")
        print("11. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            num_students = int(input("\nEnter number of students: "))
            for i in range(0, num_students):
                id = input("\nEnter student " +  str(i+1)  + " ID: ")
                name = input("Enter student " +  str(i+1)  + " name: ")
                dob = input("Enter student " +  str(i+1)  + " date of birth: ")
                Student(id, name, dob)
                Student.insert_info(id, name, dob)
                print(Student(id, name, dob))

        elif choice == 2:
            Student.modify_student_info()

        elif choice == 3:
            num_courses = int(input("\nEnter number of courses: "))
            for i in range(0, num_courses):
                id = input("\nEnter course " +  str(i+1)  + " ID: ")
                name = input("Enter course " +  str(i+1)  + " name: ")
                Course(id, name)
                Course.insert_info(id, name)
                print(Course(id, name))

        elif choice == 4:
            Course.remove_course()

        elif choice == 5:
            print(len(Student.student_list))
            Student_Management.add_student_to_course()

        elif choice == 6:
            Student_Management.remove_student_from_course()

        elif choice == 7:
            Student_Management.insert_mark_to_student()

        elif choice == 8:
            Student.display_student()     

        elif choice == 9:
            Course.display_course()

        elif choice == 10:
            Student_Management.display_mark_table()

        elif choice == 11:
            exit()

        else:
            print("Invalid choice")

while True:
    Student_Management.main()