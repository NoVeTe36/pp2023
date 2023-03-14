import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from tabulate import tabulate
import numpy as np
import math

class get_info:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __str__(self):
        return f"{self.id} {self.name}"

class Student(get_info):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.dob = dob

    def __str__(self):
        return super().__str__() + f" {self.dob}"
    
class Course(get_info):
    def __init__(self, id, name, credit):
        super().__init__(id, name)
        self.credit = credit

    def __str__(self):
        return super().__str__() + f" {self.credit}"
    
class Student_Management(Student, Course):
    # make a GUI for this class using curses module
    def __init__(self):
        self.student_list = []
        self.course_list = []
    
    def create_student(self, stdscr):
        # input number of student, then input id, name, dob respectively
        stdscr.clear()
        stdscr.addstr(1, 2, "Create Student")
        stdscr.addstr(3, 2, "Enter number of student:")
        num = int(stdscr.getstr())   
        stdscr.addstr(4, 2, "Press any key to continue")
        # enter student id, name, dob
        for i in range(0, num):
            # renew the screen to input next student          
            stdscr.refresh()
            stdscr.getch()
            stdscr.clear()  
            student_dict = {}
            count = 0
            # create each student as a dict and then append to the student list
            stdscr.addstr(4, 2, "Enter student " + str(i + 1) + " ID: ")
            id = stdscr.getstr().decode()
            # check if the student id already exists
            for j in range(0, len(self.student_list)):
                if id in self.student_list[j]['ID']:
                    count += 1
            if count != 0:
                stdscr.addstr(7, 2, "*** Student ID already exists ***")
                stdscr.addstr(8, 2, "Press any key to continue")
                continue
            if count == 0:
                stdscr.addstr(5, 2, "Enter student " + str(i + 1) + " name: ")
                name = stdscr.getstr().decode()
                stdscr.addstr(6, 2, "Enter student " + str(i + 1) + " dob: ")
                dob = stdscr.getstr().decode()
                student_dict["ID"] = id
                student_dict["Name"] = name
                student_dict["DOB"] = dob
                self.student_list.append(student_dict)
                stdscr.addstr(7, 2, f"Student {name} created")
                stdscr.addstr(8, 2, "Press any key to continue")
        self.student_list.sort(key = lambda x: x["ID"])
        stdscr.addstr(10, 2, "Press any key to continue")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
    
    def modify_student(self, stdscr):
        # print the student list and ask for student id to modify
        stdscr.clear()
        stdscr.addstr(1, 2, "Modify Student")
        student_table = tabulate(self.student_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')
        stdscr.addstr(3, 0, student_table)
        table_height = 2
        for i in range(0, len(self.student_list)): 
            for j in range(0, len(self.student_list[i])):
                table_height += 1
        stdscr.addstr(2, 2, "Enter student ID to modify: ")
        id = stdscr.getstr().decode()
        # find the student id in the student list
        for i in range(0, len(self.student_list)):
            if self.student_list[i]["ID"] == id:
                stdscr.addstr(table_height + 4, 2, "Modify Student")
                # modify all the information of the student
                stdscr.addstr(table_height + 5, 2, "Enter new student ID: ")
                id = stdscr.getstr().decode()
                stdscr.addstr(table_height + 6, 2, "Enter new student name: ")
                name = stdscr.getstr().decode()
                stdscr.addstr(table_height + 7, 2, "Enter new student dob: ")
                dob = stdscr.getstr().decode()
                self.student_list[i]["ID"] = id
                self.student_list[i]["Name"] = name
                self.student_list[i]["DOB"] = dob
                stdscr.addstr(table_height + 9, 2, f"Student {name} modified")
                stdscr.addstr(table_height + 10, 2, "Press any key to continue")
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
                break
            elif i == len(self.student_list) - 1:
                stdscr.addstr(table_height + 4, 2, "*** Student ID not found ***")
                stdscr.addstr(table_height+ 5, 2, "Press any key to continue")
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
        self.student_list.sort(key = lambda x: x["ID"])
        
    def print_student(self, stdscr):
        stdscr.clear()
        stdscr.addstr(1, 0, "Press any key to continue")
        data = tabulate(self.student_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')
        stdscr.addstr(3, 0, data)
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()

    def create_course(self, stdscr):
        # input number of course, then input id, name, credit respectively
        stdscr.clear()
        stdscr.addstr(1, 2, "Create Course")
        stdscr.addstr(3, 2, "Enter number of course:")
        num = int(stdscr.getstr())   
        stdscr.addstr(4, 2, "Press any key to continue")
        # enter course id, name, credit
        for i in range(0, num):
            # renew the screen to input next course          
            stdscr.refresh()
            stdscr.getch()
            stdscr.clear()  
            course_dict = {}
            count = 0
            # create each course as a dict and then append to the course list
            stdscr.addstr(4, 2, "Enter course " + str(i + 1) + " ID: ")
            id = stdscr.getstr().decode()
            stdscr.addstr(5, 2, "Enter course " + str(i + 1) + " name: ")
            name = stdscr.getstr().decode()
            stdscr.addstr(6, 2, "Enter course " + str(i + 1) + " credit: ")
            credit = stdscr.getstr().decode()
            course_dict["ID"] = id
            for j in range(0, len(self.course_list)):
                if self.course_list[j]["ID"] == id:
                    count += 1
            if count != 0:
                stdscr.addstr(7, 2, "*** Course ID already exists ***")
                stdscr.addstr(8, 2, "Press any key to continue")
                stdscr.getch()
                continue
            if count == 0:
                course_dict["Name"] = name
                course_dict["Credit"] = credit
                self.course_list.append(course_dict)
                stdscr.addstr(7, 2, f"Course {name} created")
                stdscr.addstr(8, 2, "Press any key to continue")
        self.course_list.sort(key = lambda x: x["ID"])
    
    def print_course(self, stdscr):
        stdscr.clear()
        stdscr.addstr(1, 0, "Press any key to continue")
        data = tabulate(self.course_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')
        stdscr.addstr(3, 0, data)
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
    
    def modify_course(self, stdscr):
        stdscr.clear()
        # print the course list and ask for course id to modify
        stdscr.addstr(1, 2, "Modify Course")
        course_table = tabulate(self.course_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')
        stdscr.addstr(3, 0, course_table)
        table_height = 2
        for i in range(0, len(self.course_list)): 
            for j in range(0, len(self.course_list[i])):
                table_height += 1
        stdscr.addstr(table_height + 3, 2, "Enter course ID to modify: ")
        id = stdscr.getstr().decode()
        # find the course id in the course list
        for i in range(0, len(self.course_list)):
            if self.course_list[i]["ID"] == id:
                stdscr.addstr(table_height + 4, 2, "Modify Course")
                # modify all the information of the course
                stdscr.addstr(table_height + 5, 2, "Enter new course ID: ")
                id = stdscr.getstr().decode()
                stdscr.addstr(table_height + 6, 2, "Enter new course name: ")
                name = stdscr.getstr().decode()
                stdscr.addstr(table_height + 7, 2, "Enter new course credit: ")
                credit = stdscr.getstr().decode()
                self.course_list[i]["ID"] = id
                self.course_list[i]["Name"] = name
                self.course_list[i]["Credit"] = credit
                stdscr.addstr(table_height + 8, 2, f"Course {name} modified")
                self.student_list.sort(key = lambda x: x["ID"])
                stdscr.addstr(table_height + 9, 2, "Press any key to continue")
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
                break
            elif i == len(self.course_list) - 1:
                stdscr.addstr(table_height + 5, 2, "*** Course ID not found ***")
                stdscr.addstr(table_height +6, 2, "Press any key to continue")
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
    
    def add_student_to_course(self, stdscr):
        stdscr.clear()
        stdscr.addstr(1, 2, "Add student to course")
        stdscr.addstr(2, 2, "Course list available: ")
        course_table = tabulate(self.course_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')
        stdscr.addstr(4, 0, course_table)
        table_height = 3
        # find the course id in the course list
        for i in range(0, len(self.course_list)): 
            for j in range(0, len(self.course_list[i])):
                table_height += 1
        stdscr.addstr(table_height + 3, 2, "Enter course ID: ")
        id = stdscr.getstr().decode()
        # print student table
        stdscr.clear()
        table_height = 3
        stdscr.addstr(1, 2, "Student list available: ")
        student_table = tabulate(self.student_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')
        stdscr.addstr(3, 0, student_table)
        for i in range(0, len(self.student_list)):
            for j in range(0, len(self.student_list[i])):
                table_height += 1
        stdscr.addstr(table_height + 3, 2, "Enter student ID: ")
        student_id = stdscr.getstr().decode()
        stdscr.addstr(table_height + 4, 2, student_id)
        student_id = student_id.split()
        student_id.sort()
        count = 0
        # check if the student id is in the course list 
        for i in range(0, len(self.course_list)):
            if id == self.course_list[i]["ID"]:
                for j in range(0, len(self.course_list[i])):
                    if 'Student' in self.course_list[i].keys():
                        for k in range(0, len(self.course_list[i]['Student'])):
                            for l in range(0, len(student_id)):
                                if student_id[l] == self.course_list[i]['Student'][k]:
                                    stdscr.addstr(table_height + 5, 2, f"Student {student_id[l]} already in course {id}")
                                    # del student_id[l] # delete the student id that is already in the course
                                    student_id.remove(student_id[l])
                                    break
        for i in range(0, len(self.course_list)):
            if id == self.course_list[i]["ID"]:
                for j in range(0, len(student_id)):
                    for k in range (0, len(self.student_list)):
                        if student_id[j] == self.student_list[k]["ID"]:
                            count += 1
                            break
                    if count != 0:
                        if 'Student' in self.course_list[i].keys():
                            self.course_list[i]['Student'].append(student_id[j])
                        else:
                            self.course_list[i]['Student'] = [student_id[j]]
                        self.course_list[i]['Student'].sort()
                stdscr.addstr(table_height + 5, 2, f"Student {student_id} added to course {id}")
        ### Also add course id, name, credit as dict to student list
        for i in range(0, len(self.course_list)):
            if id in self.course_list[i]["ID"]:
                for j in range(0, len(student_id)):
                    for k in range (0, len(self.student_list)):
                        if student_id[j] == self.student_list[k]["ID"]:
                            if 'Course' in self.student_list[k].keys():
                                self.student_list[k]['Course'].append(id)
                                self.student_list[k]['Credit'].append(self.course_list[i]['Credit'])
                            else:
                                self.student_list[k]['Course'] = [id]
                                self.student_list[k]['Credit'] = [self.course_list[i]['Credit']]

        if count == 0:
            stdscr.addstr(table_height + 8, 2, f"Student {student_id} not found")
        stdscr.addstr(table_height + 6, 2, "Press any key to continue")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()                            
                    
    def remove_student_from_course(self, stdscr):
        stdscr.clear()
        # print the student list and ask for student id to remove course
        stdscr.addstr(1, 2, "Remove Course from Student")
        course_table = tabulate(self.course_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')
        stdscr.addstr(4, 0, course_table)
        table_height = 3
        for i in range(0, len(self.course_list)): 
            for j in range(0, len(self.course_list[i])):
                table_height += 1
        stdscr.addstr(table_height + 3, 2, "Enter course ID: ")
        course_id = stdscr.getstr().decode()
        stdscr.clear()
        count_course = 0
        # print "Student list available"
        for i in range(0, len(self.course_list)):
            if course_id in self.course_list[i]['ID']:
                count_course += 1
                stdscr.addstr(1, 2, "Student list available: ")
                student_table = tabulate(self.course_list[i]['Student'], headers='Student in course', tablefmt='fancy_grid', stralign='center', numalign='center')
                stdscr.addstr(3, 0, student_table)
        if count_course == 0:
            stdscr.addstr(table_height + 5, 2, f" {course_id} not found")
        else:
            table_height = 3
            for i in range(0, len(self.student_list)):
                for j in range(0, len(self.student_list[i])):
                    table_height += 1
            stdscr.addstr(table_height + 3, 2, "Enter student ID: ")
            student_id = stdscr.getstr().decode()
            student_id = student_id.split()
            student_id.sort()
            for i in range(0, len(self.course_list)):
                if course_id in self.course_list[i]['ID']:
                    for j in range(0, len(student_id)):
                        if 'Student' in self.course_list[i]:
                            for k in range(0, len(self.course_list[i]['Student'])):
                                    if student_id[j] == self.course_list[i]['Student'][k]:
                                        stdscr.addstr(table_height + 5, 2, f"Student {student_id} removed from course {course_id}")
                                        self.course_list[i]['Student'].remove(student_id[j])
                                        break
        stdscr.addstr(table_height + 6, 2, "Press any key to continue")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()

    average_of_courses_list = []
    def add_mark_to_student(self, stdscr):
        stdscr.clear()
        # print the student list and ask for student id to add mark
        stdscr.addstr(1, 2, "Add mark to student")
        course_with_student = []
        #check if the course has student
        for i in range(len(self.course_list)):
            if 'Student' in self.course_list[i]:
                course_with_student.append(self.course_list[i])
        stdscr.addstr(2, 2, "Course list available: ")
        course_table = tabulate(course_with_student, headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')
        stdscr.addstr(4, 0, course_table)
        table_height = 3
        for i in range(0, len(course_with_student)):
            for j in range(0, len(course_with_student[i])):
                table_height += 1
        stdscr.addstr(table_height + 6, 2, "Enter course ID: ")
        course = stdscr.getstr().decode()
        table_height = 3
        for i in range(0, len(course_with_student)):
            if course == course_with_student[i]["ID"]:
                for j in range(0, len(course_with_student[i])):
                    table_height += 1
        if table_height == 3:
            stdscr.addstr(table_height + 5, 2, f" {id} not found")
        else:
            stdscr.clear()
            table_height = 3
            stdscr.addstr(2 , 2, "Student list available: ")
            # print student list in the chosen course
            course_data = None
            for i in range (0, len(course_with_student)):
                for data in course_data:
                    if data['ID'] == course:
                        course_data = data
                        break
            student_table = tabulate([course_data], headers='Student in course', tablefmt='fancy_grid', stralign='center', numalign='center')
            stdscr.addstr(4, 0, student_table)
                    
            # display student id and add mark to them respectively in the chosen course
            for i in range(0, len(self.course_list)):
                for j in range(0, len(course_with_student[i]['Student'])):
                    if course == course_with_student[i]['ID']:
                        table_height += len(course_with_student[i]['Student'])
                        stdscr.addstr(table_height + 10, 2, f"Enter mark for student {course_with_student[i]['Student'][j]}: ")
                        mark = stdscr.getstr().decode()
                        mark = mark.split()
                        mark = [float(x) for x in mark]
                        mark = [math.floor(i * 10) / 10 for i in mark]
                        avg = []
                        average = sum(mark)/len(mark)
                        average = math.floor(average * 10) / 10
                        avg.append(average)
                        # add mark to 'Mark' in the course list
                        if course == self.course_list[i]['ID']:
                            if 'Mark' in self.course_list[i]:
                                self.course_list[i]['Mark'].append(mark)
                            else:
                                self.course_list[i]['Mark'] = [mark]
                            # append average to the course list
                            if 'Average' in self.course_list[i]:
                                self.course_list[i]['Average'].append(avg)
                            else:
                                self.course_list[i]['Average'] = [avg]
                    if self.course_list[i]['ID'] == course:
                        for k in range(0, len(self.course_list[i]['Student'][j])):
                            for l in range(0, len(self.student_list)):
                                if self.course_list[i]['Student'][j] == self.student_list[l]['ID']:
                                    if 'Average' in self.student_list[l]:
                                        self.student_list[l]['Average'].append(avg)
                                    else:
                                        self.student_list[l]['Average'] = [avg]
            # reset data
            table_height = 3
            course_table = []
            student_table = []
            stdscr.clear()       

    def print_a_course_detail(self, stdscr):
        stdscr.clear()
        # display course list with headers are 'ID', 'Name', 'Credit'
        stdscr.addstr(1, 2, "Print a specific course")
        course_table = tabulate(self.course_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')
        stdscr.addstr(4, 0, course_table)
        table_height = 3
        for i in range(0, len(self.course_list)):
            for j in range(0, len(self.course_list[i])):
                table_height += 1
        stdscr.addstr(table_height + 3, 2, "Enter course ID: ")
        course_id = stdscr.getstr().decode()
        # check if the course id is in the course list
        table_height = 3
        for i in range(0, len(self.course_list)):
            if course_id == self.course_list[i]["ID"]:
                for j in range(0, len(self.course_list[i])):
                    table_height += 1
        if table_height == 3:
            stdscr.addstr(table_height + 5, 2, f" {id} not found")
        else:
            stdscr.clear()
            table_height = 3
            stdscr.addstr(2 , 2, "Course detail: ")
            for j in range(0, len(self.course_list)):
                if course_id == self.course_list[j]['ID']:
                    course_detail = tabulate(self.course_list[j], headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')
            stdscr.addstr(4, 0, course_detail)
            stdscr.addstr(8, 2, "Press any key to continue...")
            stdscr.getch()
            stdscr.clear()

    def print_student_GPA(self, stdscr):
        # GPA = (sum of all marks) / (sum of credits of courses that student has taken)
        stdscr.clear()
        stdscr.addstr(1, 2, "Print student GPA")
        # first, calculate the GPA of each student
        # GPA = (sum of all marks) / (sum of credits of courses that student has taken)
        for i in range(0, len(self.student_list)):
            if 'Average' in self.student_list[i]:
                average = np.array(self.student_list[i]['Average'])
                credit = np.array(self.student_list[i]['Credit'])
                gpa = np.sum(average * credit) / np.sum(credit)
                gpa = math.floor(gpa * 10) / 10
                if 'GPA' in self.student_list[i]:
                    self.student_list[i]['GPA'].append(gpa)
                else:
                    self.student_list[i]['GPA'] = [gpa]
        student_table = tabulate(self.student_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')
        stdscr.addstr(4, 0, student_table)

    def print_student_ranking_on_GPA(self, stdscr):
        stdscr.clear()
        stdscr.addstr(1, 2, "Print student ranking on GPA")
        # sort the student list by GPA
        self.student_list = sorted(self.student_list, key=lambda k: k['GPA'], reverse=True)
        student_table = tabulate(self.student_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')
        stdscr.addstr(4, 0, student_table)

    def run(self, stdscr):
            while True:
                stdscr.clear()
                rectangle(stdscr, 0, 0, 22, 50)
                # print a line below the title
                stdscr.addstr(2, 1, "_" * 49)                
                stdscr.addstr(1, 16, "Student Management")
                stdscr.addstr(4, 2, "1. Create Student")
                stdscr.addstr(5, 2, "2. Modify Student")
                stdscr.addstr(6, 2, "3. Print student list")
                stdscr.addstr(7, 2, "4. Create Course") 
                stdscr.addstr(8, 2, "5. Modify Course")
                stdscr.addstr(9, 2, "6. Print course list")
                stdscr.addstr(10, 2, "7. Add student to course")
                stdscr.addstr(11, 2, "8. Remove student from course")
                stdscr.addstr(12, 2, "9. Add mark to student")
                stdscr.addstr(13, 2, "q. Modify mark of student")
                stdscr.addstr(14, 2, "w. Print student mark & average in course")
                stdscr.addstr(15, 2, "e. Print student GPA")
                stdscr.addstr(16, 2, "r. Print student ranking on GPA")
                stdscr.addstr(17, 2, "t. Exit")
                stdscr.addstr(18, 1, "_" * 49)     
                stdscr.addstr(20, 2, "Enter your choice: ")
                stdscr.refresh()
                key = stdscr.getch()
                if key == ord("1"):
                    curses.echo()
                    self.create_student(stdscr)
                elif key == ord("2"):
                    curses.echo()
                    self.modify_student(stdscr)
                elif key == ord("3"):
                    curses.echo()
                    self.print_student(stdscr)
                elif key == ord("4"):
                    curses.echo()
                    self.create_course(stdscr)
                elif key == ord("5"):
                    curses.echo()
                    self.modify_course(stdscr)
                elif key == ord("6"):
                    curses.echo()
                    self.print_course(stdscr)
                elif key == ord("7"):
                    curses.echo()
                    self.add_student_to_course(stdscr)
                elif key == ord("8"):
                    curses.echo()
                    self.remove_student_from_course(stdscr)
                elif key == ord("9"):
                    curses.echo()
                    self.add_mark_to_student(stdscr)
                elif key == ord("q"):
                    curses.echo()
                    self.modify_mark_of_student(stdscr)
                elif key == ord("w"):
                    curses.echo()
                    self.print_a_course_detail(stdscr)
                elif key == ord("e"):
                    curses.echo()
                    self.print_student_GPA(stdscr)
                elif key == ord("r"):
                    curses.echo()
                    self.print_student_ranking_on_GPA(stdscr)
                elif key == ord("t"):
                    curses.echo()
                    break
                else:
                    stdscr.addstr(7, 2, "Invalid input")
                    stdscr.getch()       

def main(stdscr):
    stdscr.clear()
    management = Student_Management()
    management.run(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)