import math
from input import student_list, course_list
#list courses
def lc():
    if len(course_list) > 0:
        for course in course_list:
            if course == 0: print('No course information')
            else: print(course)
    else: print('There is no course')
#list students
def ls():
    if len(student_list) > 0:
        for student in student_list:
            if student == 0: print('No student information')
            else: print(student)
    else: print('There is no student')
#show student marks for a given course
def ssmfagc():
    minilc()
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
            try:
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
                    gpa = gpa*10
                    if gpa % 10 < 5: gpa = math.floor(gpa)/10
                    else: gpa = math.ceil(gpa)/10
                    student_list[i].set_gpa(gpa)
                    i += 1
                student_list.sort(reverse = True, key = key)
            except AttributeError: print('Please input student and course information first')
        ls()
#general course listing function for selecting
def minilc():
    if not len(course_list) > 0: print('', end ='')
    else:
        i = 1
        for course in course_list:
            if course == 0: print(str(i)+'.'+'No course information')
            else: print(str(i)+'.'+str(course.get_id()))
            i += 1
#general sorting key function
def key(student):
    return student.get_gpa()