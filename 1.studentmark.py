number_of_students = []
number_of_courses = []
#input number of students
def inosiac(n):
    n = [None]*n
    return number_of_students.append(n)
#input students informations
def isi():
    i = 0
    while i < len(number_of_students):
        number_of_students[i] = {
            "id": input("Student's id: "),
            "name": input("Student's name: "),
            "dob": input("Student's dob: "),
            "kidney": input("Number of remaining kidneys: ")
        }
        i = i + 1
#input number of courses
def inoc(n):
    n = [None]*n
    return number_of_courses.append(n)
#input courses information
def ici():
    i = 0
    while i < len(number_of_courses):
        number_of_courses[i] = {
            "id": input("Course's id: "),
            "name": input("Course's name: ")
        }
        i = i + 1
#select a course, input marks for student in this course
def sacimfasitc(n):
    course_marks = [None]*len(number_of_students)
    i = 0
    while i < len(number_of_students):
        course_marks[i] = [(number_of_students[i]["name"]+": "+str(int(input('Input marks for student '+(number_of_students[i]["id"]+':')))))]
        i = i + 1
    number_of_courses[n-1].update({"marks": course_marks})
#print number of courses
def lc():
    print(number_of_courses)
#print number of students
def ls():
    print(number_of_students)
#show student marks for a course
def ssmfagc(n):
    print(number_of_courses[n-1]["marks"])
#call functions
inosiac(int(input('Input number of students in the class:')))
isi()
inoc(int(input('Input number of courses:')))
ici()
sacimfasitc(int(input('Select course number: ')))
lc()
ls()
ssmfagc(int(input('Select course number: ')))