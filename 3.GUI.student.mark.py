import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from tabulate import tabulate

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
    
class StudentManagement(Student, Course):
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
            stdscr.addstr(5, 2, str(len(self.student_list)))
            for j in range(0, len(self.student_list)):
                if self.student_list[j] == id:
                    count += 1
            if count != 0:
                stdscr.addstr(7, 2, "*** Student ID already exists ***")
                stdscr.addstr(8, 2, "Press any key to continue")
                stdscr.getch()
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
    
    def modify_student(self, stdscr):
        # print the student list and ask for student id to modify
        stdscr.clear()
        stdscr.addstr(1, 2, "Modify Student")
        table = tabulate(self.student_list, headers='keys', tablefmt='fancy_grid', stralign='center', numalign='center')
        stdscr.addstr(4, 0, table)
        table_height = len(self.student_list) + 10
        stdscr.addstr(table_height, 2, "Enter student ID to modify: ")
        id = stdscr.getstr().decode()
        stdscr.addstr(table_height + 2, 2, "Press any key to continue")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
        # find the student id in the student list
        for i in range(0, len(self.student_list)):
            if self.student_list[i]["ID"] == id:
                stdscr.addstr(1, 2, "Modify Student")
                # modify all the information of the student
                stdscr.addstr(3, 2, "Enter new student ID: ")
                id = stdscr.getstr().decode()
                stdscr.addstr(4, 2, "Enter new student name: ")
                name = stdscr.getstr().decode()
                stdscr.addstr(5, 2, "Enter new student dob: ")
                dob = stdscr.getstr().decode()
                self.student_list[i]["ID"] = id
                self.student_list[i]["Name"] = name
                self.student_list[i]["DOB"] = dob
                stdscr.addstr(6, 2, f"Student {name} modified")
                stdscr.addstr(7, 2, "Press any key to continue")
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
                break
            elif i == len(self.student_list) - 1:
                stdscr.addstr(4, 2, "*** Student ID not found ***")
                stdscr.addstr(5, 2, "Press any key to continue")
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
        
    def print_student(self, stdscr):
        stdscr.clear()
        stdscr = curses.initscr()
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
    
    def modify_course(self, stdscr):
        # print the course list and ask for course id to modify
        stdscr.addstr(1, 2, "Modify Course")
        stdscr.addstr(3, 2, "Enter course ID to modify: ")
        id = stdscr.getstr().decode()
        stdscr.addstr(4, 2, "Press any key to continue")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
        # find the course id in the course list
        for i in range(0, len(self.course_list)):
            if self.course_list[i]["ID"] == id:
                stdscr.addstr(1, 2, "Modify Course")
                # modify all the information of the course
                stdscr.addstr(3, 2, "Enter new course ID: ")
                id = stdscr.getstr().decode()
                stdscr.addstr(4, 2, "Enter new course name: ")
                name = stdscr.getstr().decode()
                stdscr.addstr(5, 2, "Enter new course credit: ")
                credit = stdscr.getstr().decode()
                self.course_list[i]["ID"] = id
                self.course_list[i]["Name"] = name
                self.course_list[i]["Credit"] = credit
                stdscr.addstr(6, 2, f"Course {name} modified")
                self.student_list.sort(key = lambda x: x["ID"])
                stdscr.addstr(7, 2, "Press any key to continue")
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
                break
            elif i == len(self.course_list) - 1:
                stdscr.addstr(4, 2, "*** Course ID not found ***")
                stdscr.addstr(5, 2, "Press any key to continue")
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()

    def run(self, stdscr):
            while True:
                stdscr.clear()
                curses.noecho()
                curses.cbreak()
                rectangle(stdscr, 0, 0, 20, 30)
                stdscr.addstr(1, 6, "Student Management")
                stdscr.addstr(3, 2, "1. Create Student")
                stdscr.addstr(4, 2, "2. Modify Student")
                stdscr.addstr(5, 2, "3. Print student list")
                stdscr.addstr(6, 2, "4. Create Course")
                stdscr.addstr(7, 2, "5. Modify Course")
                stdscr.addstr(8, 2, "6. Print course list")
                stdscr.addstr(9, 2, "7. Exit")
                stdscr.addstr(10, 2, "Enter your choice: ")
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
                    self.modify_course(stdscr)
                elif key == ord("7"):
                    curses.echo()
                    break
                else:
                    stdscr.addstr(7, 2, "Invalid input")
                    stdscr.getch()       

def main(stdscr):
    stdscr.clear()
    management = StudentManagement()
    management.run(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)