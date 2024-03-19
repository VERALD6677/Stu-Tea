class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'

    def counting_grades(self):
        lst_grades = self.grades['Python']
        amount_lst = sum(lst_grades)
        average_rating = amount_lst / len(lst_grades)
        average = round(average_rating, 2)
        return average

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: ' \
                       f'{student_best.counting_grades()}\n' \
                       f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: ' \
                       f'{" ".join(self.finished_courses)}'
        return some_student
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}

    def calculation_grades(self):
        values = self.course_grades['Python']
        sum_lst = sum(values)
        midle_grade = sum_lst / len(values)
        return midle_grade

    def __str__(self):
        self.some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: ' \
                             f'{cool_lecturer.calculation_grades()}'
        return self.some_lecturer

    def __str1__(self):
        self.some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: ' \
                             f'{cool_lecturer1.calculation_grades()}'
        return self.some_lecturer

    def __eq__(self):
        return (cool_lecturer.calculation_grades() == cool_lecturer1.calculation_grades())

    def __ge__(self):
        return (cool_lecturer.calculation_grades() >= cool_lecturer1.calculation_grades())

    def __lt__(self):
        return (cool_lecturer.calculation_grades() < cool_lecturer1.calculation_grades())


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        self.some_reviever = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return self.some_reviever
 
student_best = Student('John', 'Salivan', 'Famale')
student_best.courses_in_progress += ['Python', 'Git']
student_best.finished_courses += ['Files']

cool_lecturer = Lecturer('Mike', 'Vazovski')
cool_lecturer.courses_attached += ['Python']

student_best.rate(cool_lecturer, 'Python', 10)
student_best.rate(cool_lecturer, 'Python', 8)
student_best.rate(cool_lecturer, 'Python', 9)

student_best = Student('John', 'Salivan', 'Famale')
student_best.courses_in_progress += ['Python']
student_best.finished_courses += ['Files']

cool_lecturer1 = Lecturer('Mih', 'Smash')
cool_lecturer1.courses_attached += ['Python']

student_best.rate(cool_lecturer1, 'Python', 10)
student_best.rate(cool_lecturer1, 'Python', 8)
student_best.rate(cool_lecturer1, 'Python', 9)

some_reviewer = Reviewer('Jimi', 'Acha-Acha')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(student_best, 'Python', 7)
some_reviewer.rate_hw(student_best, 'Python', 9)
some_reviewer.rate_hw(student_best, 'Python', 10)

print('Student:')
print(student_best.__str__())
print('Lecturer:')
print(cool_lecturer.__str__())
print(cool_lecturer1.__str1__())
print('Равныли срение оценки лекторов:')
print(cool_lecturer.__eq__() == cool_lecturer1.__eq__())
print('Средняя оценка первого лектора больше или ровна средней оценки второго:')
print(cool_lecturer.__ge__() >= cool_lecturer1.__ge__())
print('Средняя оценка первого лектора меньше средней оценки второго:')
print(cool_lecturer.__lt__() < cool_lecturer1.__lt__())
print('Reviewer:')
print(some_reviewer.__str__())
