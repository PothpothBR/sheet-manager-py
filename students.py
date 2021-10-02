from io_format import *

# round up a number
roundup = lambda n: int(n+0.9)


# class to manage student data
class Students:

    # generate all data here
    def __init__(self, data: list):
        # get the school days
        tmp_days = str()
        for i in data[0][0][0]:
            if i.isnumeric():
                tmp_days += i

        self.days = int(tmp_days)

        # get the absences days, grades and names
        self.absences = list()
        self.grades = list()
        self.names = list()
        for i in data[1:]:
            self.absences.append(int(i[2]))
            self.grades.append([int(i[3]), int(i[4]), int(i[5])])
            self.names.append(i[1])

        # get the status of the grade and, if necessary, grade for final approval
        self.situations = list()
        self.NAF = list()
        for i in range(len(self.names)):
            self.NAF.append(0)
            self.situations.append(self.__student_situation__(i))

    # return the student semester situation
    def __student_situation__(self, id: int) -> str:

        # error catch
        if id < 0 or id > len(self.names):
            exif('student id invalid')

        # verify student situation about the absences
        if self.absences[id] * 100 / self.days > 25:
            return 'Reprovado por Falta'

        # generate average grade
        avg = (self.grades[id][0] + self.grades[id][1] + self.grades[id][2]) / 3

        # verify student situation, if in dependence, generate minimum final grade
        if avg < 50:
            return 'Reprovado pot Nota'
        elif 50 <= avg < 70:
            self.NAF[id] = roundup(140 - avg)
            return 'Exame Final'
        elif avg >= 70:
            return 'Aprovado'
