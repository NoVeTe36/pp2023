import numpy as np
import math
from tabulate import tabulate
import curses
from curses import wrapper

class get_info:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return f"\nID: {self.id}\nName: {self.name}"


class Student(get_info):
    student_list = []

    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.dob = dob
    
    def insert_info(id, name, dob):
        #check if student already exists
        count = 0
        for i in range(0, len(Student.student_list)):
            if Student.student_list[i]['ID: '] == id:
                count += 1
                break
        if count == 0:
            student_dict = {}
            student_dict['ID: '] = id
            student_dict['Name: '] = name
            student_dict['Date of birth: '] = dob
            Student.student_list.append(student_dict)
            Student.student_list = sorted(Student.student_list, key=lambda i: i['ID: '])
            print(Student(id, name, dob))
        else:
            print("\n***Student already exists***\n")

    def __str__(self):
        return super().__str__() + f"\nDate of birth: {self.dob}"
    
    def modify_student_info():
        print("List of student\n:")
        print("ID\t\t\tName\t\t\t\tDate of birth")
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

    def display_student():
        Student.student_list = sorted(Student.student_list, key=lambda i: i['ID: '])
        print(tabulate(Student.student_list, headers="keys", tablefmt="fancy_grid", numalign= "center", stralign= "center"))
    
class Course(get_info):
    course_list = []
    credits = []
    def __init__(self, id, name, credit):
        super().__init__(id, name)
        self.credit = credit

    def insert_info(id, name, credit):
        course_dict = {}
        course_dict['ID: '] = id
        course_dict['Name: '] = name
        course_dict['Credit: '] = credit
        Course.course_list.append(course_dict)       

    def __str__(self):
        return super().__str__() + f"\nCredit: {self.credit}"

    def display_course():
        Course.course_list = sorted(Course.course_list, key=lambda i: i['ID: '])
        print(tabulate(Course.course_list, headers="keys", tablefmt="fancy_grid", numalign= "center", stralign= "center"))
        

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
    data_np_list = []
    average_of_courses_list = []
    def add_student_to_course():
        print("Course available: ")
        for i in range(0, len(Course.course_list)):
            print(Course.course_list[i]['ID: '])
        course = input("\nEnter course ID: \n")
        count = 0
        if len(Course.course_list) == 0:
            print("No courses available")
        else:                   
            for i in range(0, len(Course.course_list)):
                if Course.course_list[i]['ID: '] == course:
                    count += 1
                    print("List of student:")
                    for i in range(0, len(Student.student_list)):
                        print(Student.student_list[i]['ID: '])   
                    student_id = input("Enter student ID: ")
                    student_id = student_id.split()
                    student_id.sort()
                    print(student_id)
                    count_st = 0
                    for i in range(0, len(Course.course_list)):
                        if Course.course_list[i]['ID: '] == course:
                            for j in range(0, len(student_id)):
                                for k in range(0, len(Student.student_list)):
                                    if student_id[j] == Student.student_list[k]['ID: ']:
                                        count_st += 1
                                        break
                            if count_st != 0:
                                if 'Student: ' in Course.course_list[i].keys():
                                    Course.course_list[i]['Student: '][j].append(student_id[j])
                                else:
                                    Course.course_list[i]['Student: '] = [student_id[j]]
                                Course.course_list[i]['Student: '][j].sort()
                        print("Student has been added\n")

                    #add course ID, credits as a dict to student
                    for i in range(0, len(Course.course_list)):
                        if Course.course_list[i]['ID: '] == course:
                            for j in range(0, len(student_id)):
                                for k in range(0, len(Student.student_list)):
                                    if student_id[j] == Student.student_list[k]['ID: ']:
                                        if 'Course ID: ' in Student.student_list[k].keys():
                                            Student.student_list[k]['Course ID: '].append(course)
                                        else:
                                            Student.student_list[k]['Course ID: '] = [course]
                                        if 'Credit: ' in Student.student_list[k].keys():
                                            Student.student_list[k]['Credit: '].append(Course.course_list[i]['Credit: '])
                                        else:
                                            Student.student_list[k]['Credit: '] = [Course.course_list[i]['Credit: ']]
                                        break
        if count == 0:
            print("Course not found\n")
        print(tabulate(Course.course_list, headers="keys", tablefmt="fancy_grid", numalign= "center", stralign= "center"))
    
    def remove_student_from_course():
        print("Course available: ")
        for i in range(0, len(Course.course_list)):
            print(Course.course_list[i])
        course = input("Enter course ID: ")
        print("List of student:")
        for i in range(0, len(Course.course_list)):
            if course == Course.course_list[i]['ID: ']:
                for j in range(0, len(Course.course_list[i]['Student: '])):
                    print(Course.course_list[i]['Student: '][j])
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
        print(tabulate(Course.course_list, headers="keys", tablefmt="fancy_grid", numalign= "center", stralign= "center"))
    
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
                        data_np = []
                        print("Student ID: " + Course.course_list[i]['Student: '][j][k])
                        mark = (input("Enter student mark: "))
                        mark = mark.split()
                        mark = [float(i) for i in mark]
                        mark = [math.floor(i * 10) / 10 for i in mark]
                        data_np.append(mark)
                        avg = np.average(data_np)
                        Student_Management.data_np_list.append(avg)
                        if 'Mark: ' in Course.course_list[i]:
                            Course.course_list[i]['Mark: '].append(mark)              
                        else:
                            Course.course_list[i]['Mark: '] = [mark]
                        print("Mark has been added\n")
                        #calculate Average of student in each course 
                        for l in range(0, len(Student.student_list)):
                            if Course.course_list[i]['Student: '][j][k] == Student.student_list[l]['ID: ']:
                                average = 0
                                for m in range(0, len(Course.course_list[i]['Mark: '][k])):
                                    average += Course.course_list[i]['Mark: '][k][m]/len(Course.course_list[i]['Mark: '][k])
                                if 'Average: ' in Course.course_list[i]:
                                    Course.course_list[i]['Average: '].append(average)
                                else:
                                    Course.course_list[i]['Average: '] = [average]
                                if 'Average: ' in Student.student_list[l]:
                                    Student.student_list[l]['Average: '].append(average)
                                else:
                                    Student.student_list[l]['Average: '] = [average]
                        data_np = []  
        if count == 0:
            print("Student not found\n") 
        #append course, mark, average that just input to average_of_courses_list
        for i in range(0, len(Course.course_list)):
            if Course.course_list[i]['ID: '] == course:
                Student_Management.average_of_courses_list.append({'Course: ': course, 'Mark: ': Course.course_list[i]['Mark: '], 'Average: ': Course.course_list[i]['Average: ']})
        print(tabulate(Student_Management.average_of_courses_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign ='center'))


    def modify_student_mark():
        print("Course available: ")
        for i in range(0, len(Course.course_list)):
            if 'Student: ' in Course.course_list[i]:
                print(Course.course_list[i])
        course = input("Enter course ID: ")
        print("List of student:")
        for i in range(0, len(Course.course_list)):
            if Course.course_list[i]['ID: '] == course:
                for j in range(0, len(Course.course_list[i]['Student: '])):
                    print(Course.course_list[i]['Student: '][j])
                    print("\n")
        count = 0
        student_id = input("Student ID you want to modify: ")
        for i in range(0, len(Course.course_list)):
            if Course.course_list[i]['ID: '] == course:
                count += 1
                for j in range(0, len(Course.course_list[i]['Student: '])):
                    for k in range(0, len(Course.course_list[i]['Student: '][j])):
                        if Course.course_list[i]['Student: '][j][k] == student_id:
                            print("Student ID: " + Course.course_list[i]['Student: '][j][k])
                            mark = (input("Enter student mark: "))
                            mark = mark.split()
                            mark = [float(i) for i in mark]
                            mark = [math.floor(i * 10) / 10 for i in mark]
                            Course.course_list[i]['Mark: '][k] = mark
                            # re-calculate Average of student in each course
                            for l in range(0, len(Student.student_list)):
                                if Course.course_list[i]['Student: '][j][k] == Student.student_list[l]['ID: ']:
                                    average = 0
                                    for m in range(0, len(Course.course_list[i]['Mark: '][k])):
                                        average += Course.course_list[i]['Mark: '][k][m]/len(Course.course_list[i]['Mark: '][k])
                                    Course.course_list[i]['Average: '][k] = average
                                    Student.student_list[l]['Average: '][k] = average
                            print("Mark has been modified\n")
        if count == 0:
            print("Student not found\n")

    def display_mark_table_each_course():
        mark_each_course = []
        print("Course available: ")
        print(tabulate(Course.course_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign ='center'))
        course = input("Enter course ID: ")
        count = 0      
        for i in range(0, len(Course.course_list)):
            if Course.course_list[i]['ID: '] == course:
                for j in range(0, len(Course.course_list[i]['Student: '])):
                    for k in range(0, len(Course.course_list[i]['Student: '][j])):
                        for l in range(0, len(Student.student_list)):
                            if Course.course_list[i]['Student: '][j][k] == Student.student_list[l]['ID: ']:
                                count += 1
                                mark_each_course.append({'Student: ': Course.course_list[i]['Student: '][j][k], 'Name: ': Student.student_list[l]['Name: '], 'Mark: ': Course.course_list[i]['Mark: '][k], 'Average: ': Course.course_list[i]['Average: '][k]})
                        if count == 0:
                            print("Student not found")
                            break
        print(tabulate(mark_each_course, headers='keys', tablefmt='fancy_grid', stralign='center', numalign ='center'))
    
    def display_all_mark_with_gpa():
        # calculate the GPA from student table and display using tabulate 
        for i in range(0, len(Student.student_list)):
            # calculate GPA using numpy from Average array and Credit array
            if 'Average: ' in Student.student_list[i]:
                # using numpy from Average array and Credit array
                data_np_avg = Student.student_list[i]['Average: ']
                data_np_credit = Student.student_list[i]['Credit: ']
                count = np.average(data_np_avg, weights=data_np_credit)    
                if 'GPA: ' in Student.student_list[i]:
                    Student.student_list[i]['GPA: '] = count
                else:
                    Student.student_list[i].update({'GPA: ': count})       
                # reset data_np_avg and data_np_credit
                data_np_avg = []
                data_np_credit = []
        Student.student_list.sort(key=lambda x: x['ID: '])
        print(tabulate(Student.student_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign ='center'))

    def display_all_mark_with_gpa_sorted():
        #check if each student has GPA or not
        for i in range(0, len(Student.student_list)):
            if 'GPA: ' in Student.student_list[i]:
                pass
            else:
                print(1)
                Student.student_list[i]['GPA: '] = 0
                print(Student.student_list[i])
        # sort GPA from student table
        Student.student_list.sort(key=lambda x: x['GPA: '], reverse=True)
        print(tabulate(Student.student_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign ='center'))

    def main():
        print("\n1.  Add student")
        print("2.  Modify student information")
        print("3.  Add course")
        print("4.  Remove course")
        print("5.  Add student to course")
        print("6.  Remove student from course")
        print("7.  Insert mark to student")
        print("8.  Modify mark of student")
        print("9.  Display student list")
        print("10. Display course list")
        print("11. Display table mark")
        print("12. Display all mark with GPA")
        print("13. Display all mark with GPA sorted")
        print("14. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            num_students = int(input("\nEnter number of students: "))
            for i in range(0, num_students):
                id = input("\nEnter student " +  str(i+1)  + " ID: ")
                name = input("Enter student " +  str(i+1)  + " name: ")
                dob = input("Enter student " +  str(i+1)  + " date of birth: ")
                Student(id, name, dob)
                Student.insert_info(id, name, dob)
            Student.student_list = sorted(Student.student_list, key=lambda i: i['ID: '])

        elif choice == 2:
            Student.modify_student_info()

        elif choice == 3:
            num_courses = int(input("\nEnter number of courses: "))
            for i in range(0, num_courses):
                id = input("\nEnter course " +  str(i+1)  + " ID: ")
                name = input("Enter course " +  str(i+1)  + " name: ")
                credits = int(input("Enter course " +  str(i+1)  + " credits: "))
                Course(id, name, credits)
                Course.insert_info(id, name, credits)
                print(Course(id, name, credits))

        elif choice == 4:
            Course.remove_course()

        elif choice == 5:
            Student_Management.add_student_to_course()

        elif choice == 6:
            Student_Management.remove_student_from_course()

        elif choice == 7:
            Student_Management.insert_mark_to_student()

        elif choice == 8:
            Student_Management.modify_student_mark()

        elif choice == 9:
            Student.display_student()     

        elif choice == 10:
            Course.display_course()

        elif choice == 11:
            Student_Management.display_mark_table_each_course()

        elif choice == 12:
            Student_Management.display_all_mark_with_gpa()

        elif choice == 13:
            Student_Management.display_all_mark_with_gpa_sorted()

        elif choice == 14:
            exit()

        else:
            print("Invalid choice")

while True:
    Student_Management.main()