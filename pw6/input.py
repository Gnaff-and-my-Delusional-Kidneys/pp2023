from domains import Student, Course
import math
import numpy as np
import pickle
import os
#lists
student_list = []
course_list = []
#input number of students in a class
def inosiac():
    while True:
        try:
            n = int(input('Input number of students in the class: '))
            if not n > 0: print('Invalid number of students, please try again')
            else:
                if n < len(student_list): 
                    n = [0]*n
                    student_list.clear()
                else: n = [0]*(n-len(student_list))
        except ValueError:
            print('Invalid number of students, please try again')
            continue
        return student_list.extend(n)
#input students informations
def isi():
    if len(student_list) == 0: print('There is no student!')
    else:
        i = 0
        j = 0
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
                elif student_list[i].get_kidney() == 0: print('THE KIDNEYLESS')
                elif student_list[i].get_kidney() < 0: print('Kidney debt???')#No waaayyaayyaaaaae
                i += 1
            else: 
                i += 1
                j += 1
        if j == len(student_list): 
            if j == 1: print('All student have their info inputted')
            else: print('All student have their info inputted')
#input number of courses
def inoc():
    while True:
        try:
            n = int(input('Input number of courses: '))
            if not n > 0: print('Invalid number of students, please try again')
            else:
                if n < len(course_list): 
                    n = [0]*n
                    course_list.clear()
                else: n = [0]*(n-len(course_list))
        except ValueError:
            print('Invalid number of students, please try again')
            continue    
        return course_list.extend(n)
#input courses informations
def ici(): 
    if len(course_list) == 0: print('There is no course!')
    else: 
        i = 0
        j = 0
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
            else: 
                i += 1
                j += 1
        if j == len(course_list):
            if j == 1: print('All course have their info inputted')
            else: print('All courses have their info inputted')
#select a course, input marks for student in this course
def sacimfasitc():
    minilc()
    if not len(course_list) > 0: print('There is no course')
    else:
        if not len(student_list) > 0: print('There is no student')
        else:
            try:
                n = int(input('Select course number: '))
                if not n <= len(course_list) and n > 0: print('Invalid course number, please try again')
                else:
                    try:
                        marks = course_list[n-1].get_marks()
                        if len(student_list) < len(marks): 
                            n = np.zeros(len(student_list) - len(marks))
                            marks = np.concatenate(marks, n)
                        else: 
                            marks = np.zeros(len(student_list))
                        i = 0
                        while i < len(student_list):
                            if marks[i] == 0: 
                                marks[i] = float(input('Input mark for student ' + student_list[i].get_id() +': '))
                                marks[i] = marks[i]*10
                                if marks[i] % 10 < 5: marks[i] = math.floor(marks[i])/10
                                else: marks[i] = math.ceil(marks[i])/10
                            if marks[i] >= 0 and marks[i] <= 20: i += 1
                            else: print('Invalid marks input, please try again')
                        course_list[n-1].set_marks(marks)
                    except AttributeError: print("Please input course information first")
            except ValueError: print('Invalid course number, please try again')
#general course listing function for selecting
def minilc():
    if not len(course_list) > 0: print('', end ='')
    else:
        i = 1
        for course in course_list:
            if course == 0: print(str(i)+'.'+'No course information')
            else: print(str(i)+'.'+str(course.get_id()))
            i += 1
#update everything
def update_info():
    path = os.path.realpath(__file__)
    dir = os.path.dirname(path)
    dir += '\info'
    os.chdir(dir)
    outfile = open('students','wb')
    pickle.dump(student_list,outfile)
    outfile.close()
    outfile = open('courses','wb')
    pickle.dump(course_list,outfile)
    outfile.close()
#load info
def load_info():
    path = os.path.realpath(__file__)
    dir = os.path.dirname(path)
    dir += '\info'
    os.chdir(dir)
    if os.path.isfile("students"):
        infile = open('students','rb')
        n = pickle.load(infile)
        infile.close()
        student_list.extend(n)
    if os.path.isfile("courses"):
        infile = open('courses','rb')
        n = pickle.load(infile)
        infile.close()
        course_list.extend(n)