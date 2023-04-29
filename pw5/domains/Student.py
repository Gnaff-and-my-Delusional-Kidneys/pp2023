from datetime import datetime
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
        dob = datetime.strptime(dob,"%d-%m-%Y").date()
        self.__dob = dob.strftime("%d-%m-%Y")
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