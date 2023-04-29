import numpy as np
class Course:
    def __init__(self):
        self.__id = ''
        self.__name = ''
        self.__credit = 0
        self.__marks = np.array([])
    def set_course(self, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit
    def set_marks(self, marks): self.__marks = marks
    def __str__(self): return f"Course's id: {self.__id}\nCourse's name: {self.__name}\nCourse's credits: {self.__credit}\n\n"
    def get_id(self): return f'{self.__id}'
    def get_credit(self): return self.__credit
    def get_marks(self): return self.__marks