number_of_students = []
number_of_courses = []
class Student:
    def __init__(self, id, name, dob, number_of_remaining_kidneys):
        self.id = id
        self.name = name
        self.dob = dob
        self.kidney = number_of_remaining_kidneys
    def __str__(self):
        return f"Student's id: {self.id}\nStudent's name: {self.name}\nStudent's dob: {self.dob}\nStudent's number of remaining kidneys: {self.kidney}\n\n"
class Course:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks
    def __str__(self):
        return f"Course's id: {self.id}\nCourse's name: {self.name}\n\n"
#input number of students in a class
def inosiac(n):
    n = [None]*n
    return number_of_students.append(n)
#input students informations
def isi():
    i = 0
    while i < len(number_of_students):
        if number_of_students[i] == [None]:
            number_of_students[i] = Student(input("Student's id: "),
                                            input("Student's name: "),
                                            input("Student's dob: "),
                                            int(input("Student's number of remaining kidneys: ")))
            if number_of_students[i].kidney == 0:
                print('''        "Kidney on the tree
        Kindness in your heart
        Kidnap to China
        對酒當歌，人生幾何？
        画虎画皮难画骨， 知人知面不知心，            
        Bad monarch chews the dirt
        Hatred that is not our own
        I like chôm chôm."''') #a poem for the kidneyless by "The Kidneys In My Head"
        i += 1
#input number of courses
def inoc(n):
    n = [None]*n
    return number_of_courses.append(n)
#input courses informations
def ici():
    i = 0
    while i < len(number_of_courses):
        if number_of_courses[i] == [None]:
            number_of_courses[i] = Course(input("Course's id: "),
                                          input("Course's name: "),
                                          None)
        i += 1
#select a course, input marks for student in this course
def sacimfasitc(n):
    marks = [None]*len(number_of_students)
    i = 0
    while i < len(number_of_students):
        marks[i] = float(input('Input mark for student '+ number_of_students[i].id +': '))
        i += 1
    number_of_courses[n-1].marks = marks
#list courses
def lc():
    for course in number_of_courses:
        print(course)
#list students
def ls():
    for student in number_of_students:
        print(student)
#show student marks for a given course
def ssmfagc(n):
    marks = number_of_courses[n-1].marks
    i = 0
    while i < len(number_of_students):
        print(number_of_students[i].id + ": " + str(marks[i]))
        i += 1
#main fuction
def main():
    print('''What do you want to do:
    1.input number of students
    2.input students informations
    3.input number of courses
    4.input courses informations
    5.select a course, input marks for student in this course
    6.list number of courses
    7.list number of students
    8.show student marks for a given course''')
    while 0==0:
        opt = int(input()) 
        if opt == 1:
            inosiac(int(input('Input number of students in the class: ')))
        elif opt == 2:
            isi()
        elif opt == 3:
            inoc(int(input('Input number of courses: ')))
        elif opt == 4:
            ici()
        elif opt == 5:
            sacimfasitc(int(input('Select course number: ')))
        elif opt == 6:
            lc()
        elif opt == 7:
            ls()
        elif opt == 8:
            ssmfagc(int(input('Select course number: ')))
if __name__ == "__main__":
    main()
#for confirmation: i absolutely do not have any kind of obsession for kidneys