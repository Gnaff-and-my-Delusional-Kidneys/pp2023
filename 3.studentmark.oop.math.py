from datetime import datetime
import math
import numpy as np
#lists
student_list = []
course_list = []
#classes
class Student:
    def __init__(self):
        self.__id = ''
        self.__name = ''
        self.__dob = ''
        self.__kidney = None
        self.__gpa = 0
    def set_student(self, id, name, number_of_remaining_kidneys):
        self.__id = id
        self.__name = name
        self.__kidney = number_of_remaining_kidneys
    def set_dob(self, dob):
        try:
            dob = datetime.strptime(dob,"%d-%m-%Y").date()
        except ValueError: print("Invalid student's date of birth, please try again")
        else: self.__dob = dob.strftime("%d-%m-%Y")
    def set_gpa(self, gpa): self.__gpa = gpa
    def __str__(self): return f"""Student's id: {self.__id}
Student's name: {self.__name}
Student's dob: {self.__dob}
Student's number of remaining kidneys: {self.__kidney}
Student's average GPA: {self.__gpa}

"""
    def get_id(self): return f'{self.__id}'
    def get_kidney(self): return self.__kidney
    def get_gpa(self): return self.__gpa
class Course:
    def __init__(self):
        self.__id = ''
        self.__name = ''
        self.__marks = []
        self.__credit = 0
    def set_course(self, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit
    def set_marks(self, marks): self.__marks = marks
    def __str__(self): return f"Course's id: {self.__id}\nCourse's name: {self.__name}\nCourse's credits: {self.__credit}\n\n"
    def get_id(self): return f'{self.__id}'
    def get_marks(self): return self.__marks
    def get_credit(self): return self.__credit
#input number of students in a class
def inosiac():
    while True:
        try:
            n = int(input('Input number of students in the class: '))
            if n > 0:
                if n < len(student_list): n = [0]*n
                else: n = [0]*(n-len(student_list))
            else: print('Invalid number of students, please try again')
        except ValueError:
            print('Invalid number of students, please try again')
            continue
        return student_list.extend(n)
#input students informations
def isi():
    if len(student_list) == 0: print('There is no student!')
    else:
        i = 0
        while i < len(student_list):
            if student_list[i] == 0:
                if not i == 0: print()
                student_list[i] = Student()
                while True:
                    id = input("Student's id: ")
                    name = input("Student's name: ")
                    while True:
                        try: student_list[i].set_dob(input("Student's dob: "))
                        except (ValueError, TypeError): 
                            print("Invalid student's date of birth, please try again")
                            continue
                        else: break
                    while True:
                        try: number_of_remaining_kidneys = int(input("Student's number of remaining kidneys: "))
                        except ValueError: 
                            print('invalid number of remaining kidneys, please try again')
                            continue
                        else: break
                    break
                student_list[i].set_student(id, name, number_of_remaining_kidneys)
                if student_list[i].get_kidney() == 0:
                    print('''        "Kidney on the tree
        Kindness in your heart
        Kidnap to China
        對酒當歌，人生幾何？
        画虎画皮难画骨， 知人知面不知心，            
        Bad monarch chews the dirt
        Hatred that is not our own
        I like chôm chôm."
                "The Kidneys In My Head"''') #A poem for the kidneyless. P.S: i don't actually like chôm chôm
                elif student_list[i].get_kidney() == 3: print('My delusional kidney')#Wut da heeeeeeeeeeeeeeel
                elif student_list[i].get_kidney() > 3: print('My delusional kidneys')#Oooh maa gaaaad 
                elif student_list[i].get_kidney() < 0: print('Kidney debt???')#No waaayyaayyaaaaae
                i += 1
#input number of courses
def inoc():
    while True:
        try:
            n = int(input('Input number of courses: '))
            if n > 0:
                if n < len(course_list): n = [0]*n
                else: n = [0]*(n-len(course_list))
            else: print('Invalid number of students, please try again')
        except ValueError:
            print('Invalid number of students, please try again')
            continue    
        return course_list.extend(n)
#input courses informations
def ici(): 
    if len(course_list) == 0: print('There is no course!')
    else: 
        i = 0
        while i < len(course_list):
            if course_list[i] == 0:
                id = input("Course's id: ")
                name = input("Course's name: ")
                while True:
                    try:
                        credit = int(input("Course's number of credits: "))
                    except ValueError: print('Invalid number of credits, please try again')
                    else: break
                course_list[i] = Course()
                course_list[i].set_course(id, name, credit)
                i += 1
#select a course, input marks for student in this course
def sacimfasitc():
    if not len(course_list) > 0: print('There is no course')
    else:
        if not len(student_list) > 0: print('There is no student')
        else:
            try:
                n = int(input('Select course number: '))
                if not n <= len(course_list) and n > 0: print('Invalid input, please try again')
                else:
                    marks = course_list[n-1].get_marks()
                    if len(student_list) < len(marks): nl = [0]*len(student_list)
                    else: nl = [0]*(len(student_list)-len(marks))
                    marks.extend(nl)
                    i = 0
                    while i < len(student_list):
                        if marks[i] == 0: 
                            marks[i] = float(input('Input mark for student ' + student_list[i].get_id() +': '))
                            marks[i] = math.floor(marks[i]*10)/10
                        if marks[i] >= 0 and marks[i] <= 20: i += 1
                        else: print('Invalid marks input, please try again')
                    course_list[n-1].set_marks(marks)
            except ValueError: print('Invalid course number, please try again')
#list courses
def lc():
    if len(course_list) > 0:
        for course in course_list:
            print(course)
    else: print('There is no course')
#list students
def ls():
    if len(student_list) > 0:
        for student in student_list:
            print(student)
    else: print('There is no student')
#show student marks for a given course
def ssmfagc():
    if not len(course_list) > 0: print('There is no course')
    else:
        if not len(student_list) > 0: print('There is no student')
        else:
            try:
                n = int(input('Select course number: '))
                if n <= len(course_list) and n > 0:
                    marks = course_list[n-1].get_marks()
                    i = 0
                    while i < len(student_list):
                        print(student_list[i].get_id() + ": " + str(marks[i]))
                        i += 1
                else: print('Invalid input, please try again')
            except ValueError: print('Invalid input, please try again')
#calculate average GPA and sort student list by GPA descending
def cagpaastlbgpad():
    if not len(course_list) > 0: print('There is no course')
    else:
        if not len(student_list) > 0: print('There is no student')
        else:
            i = 0
            while i < len(student_list):
                gpa = 0
                total_credits = 0
                cn = 0
                while cn < len(course_list):
                    marks = course_list[cn].get_marks()
                    gpa = gpa + (marks[i] * course_list[cn].get_credit())
                    total_credits = total_credits + course_list[cn].get_credit()
                    cn += 1
                gpa /= total_credits
                gpa = math.floor(gpa*10)/10
                student_list[i].set_gpa(gpa)
                i += 1
        student_list.sort(key = key)
        ls()
#general functions
def minilc():
    if len(course_list) > 0:
        for course in course_list:
            i = 1
            print(str(i)+'.'+str(course.get_id()))
            i += 1
    else: print('', end ='')
def key(student):
    return student.get_gpa()
#main fuction
def main():
    print('''What do you want to do:
    0.exit
    1.input number of students
    2.input students informations
    3.input number of courses
    4.input courses informations
    5.select a course, input marks for student in this course
    6.list number of courses
    7.list number of students
    8.show student marks for a given course
    9.Calculate average GPA and sort student list by GPA descending''')
    while True:
        try:
            opt = int(input()) 
            if opt == 0: break
            elif opt == 1: inosiac()
            elif opt == 2: isi()
            elif opt == 3: inoc()
            elif opt == 4: ici()
            elif opt == 5:
                minilc()
                sacimfasitc()
            elif opt == 6: lc()
            elif opt == 7: ls()
            elif opt == 8:
                minilc()
                ssmfagc()
            elif opt == 9: 
                cagpaastlbgpad()
            else: print('Invalid input, please try again')
        except ValueError: 
            print('Invalid input, please try again')
            continue
if __name__ == "__main__":
    main()
#for confirmation: i absolutely do not have any kind of obsession for kidneys