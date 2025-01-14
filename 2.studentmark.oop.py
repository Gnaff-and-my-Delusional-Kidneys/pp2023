student_list = []
course_list = []
class Student:
    def __init__(self):
        self.__id = ''
        self.__name = ''
        self.__dob = ''
        self.__kidney = 0
    def set_student(self, id, name, dob, number_of_remaining_kidneys):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__kidney = number_of_remaining_kidneys
    def get_kidney(self): return self.__kidney
    def get_id(self): return f'{self.__id}'
    def __str__(self): return f"Student's id: {self.__id}\nStudent's name: {self.__name}\nStudent's dob: {self.__dob}\nStudent's number of remaining kidneys: {self.__kidney}\n\n"
class Course:
    def __init__(self):
        self.__id = ''
        self.__name = ''
        self.__marks = []
    def set_course(self, id, name):
        self.__id = id
        self.__name = name
    def set_marks(self, marks): self.__marks = marks
    def get_id(self): return f'{self.__id}'
    def get_marks(self): return self.__marks
    def __str__(self): return f"Course's id: {self.__id}\nCourse's name: {self.__name}\n\n"
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
                    dob = input("Student's dob: ")
                    try: number_of_remaining_kidneys = int(input("Student's number of remaining kidneys: "))
                    except ValueError: 
                        print('invalid number of remaining kidneys, please try again')
                        continue
                    else: break
                student_list[i].set_student(id, name, dob, number_of_remaining_kidneys)
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
                elif student_list[i].get_kidney() == 3: print('My delusional kidney')#WUT DE HEILLLLLLLLL
                elif student_list[i].get_kidney() > 3: print('My delusional kidneys')#OMG
                elif student_list[i].get_kidney() < 0: print('Poor')#NO WAYAYAYAYAYAY
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
                course_list[i] = Course()
                course_list[i].set_course(input("Course's id: "),
                                          input("Course's name: "))
            i += 1
#select a course, input marks for student in this course
def sacimfasitc():
    if len(course_list) > 0:
        if len(student_list) > 0:
            try:
                n = int(input('Select course number: '))
                if n < len(course_list) and n > 0:
                    marks = course_list[n-1].get_marks()
                    if len(student_list) < len(marks): n = [0]*len(student_list)
                    else: n = [0]*(len(student_list)-len(marks))
                    marks.extend(n)
                    i = 0
                    while i < len(student_list):
                        if marks[i] == 0: marks[i] = float(input('Input mark for student ' + student_list[i].get_id() +': '))
                        if marks[i] >= 0 and marks[i] <= 20: i += 1
                        else: print('Invalid marks input, please try again')
                    course_list[n-1].set_marks(marks)
                else: print('Invalid input, please try again')
            except ValueError: print('Invalid course number, please try again')
        else: print('There is no student')
    else: print('There is no course')
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
    if len(course_list) > 0:
        if len(student_list) > 0:
            try:
                n = int(input('Select course number: '))
                if n < len(course_list) and n > 0:
                    marks = course_list[n-1].get_marks()
                    i = 0
                    while i < len(student_list):
                        print(student_list[i].get_id() + ": " + str(marks[i]))
                        i += 1
                else: print('Invalid input, please try again')
            except ValueError: print('Invalid input, please try again')
        else: print('There is no student')
    else: print('There is no course')
#general function for selecting
def minilc():
    if len(course_list) > 0:
        for course in course_list:
            i = 1
            print(str(i)+'.'+str(course.get_id()))
            i += 1
    else: print('', end ='')
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
    8.show student marks for a given course''')
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
            else: print('Invalid input, please try again')
        except ValueError: 
            print('Invalid input, please try again')
            continue
if __name__ == "__main__":
    main()
#for confirmation: i absolutely do not have any kind of obsession for kidneys