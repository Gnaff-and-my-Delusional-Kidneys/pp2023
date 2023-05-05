from domains import Student, Course
from input import inosiac, isi, inoc, ici, sacimfasitc, update_info, load_info
from output import lc, ls, ssmfagc, cagpaastlbgpad
#main fuction
def main():
    load_info()
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
            if opt == 0: 
                update_info()
                break
            elif opt == 1: inosiac()
            elif opt == 2: isi()
            elif opt == 3: inoc()
            elif opt == 4: ici()
            elif opt == 5: sacimfasitc()
            elif opt == 6: lc()
            elif opt == 7: ls()
            elif opt == 8: ssmfagc()
            elif opt == 9: cagpaastlbgpad()
            else: print('Invalid input, please try again')
        except ValueError: 
            print('Invalid input, please try again')
            continue
#call main function
if __name__ == "__main__":
    main()
#for confirmation: i absolutely do not have any kind of obsession for kidneys