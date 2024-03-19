class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}


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
 
student_best = Student('Ruoy', 'Eman', 'your_gender')
student_best.courses_in_progress += ['Python']
 
some_reviewer = Reviewer('Jimi', 'Acha-Acha')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(student_best, 'Python', 7)
some_reviewer.rate_hw(student_best, 'Python', 9)
some_reviewer.rate_hw(student_best, 'Python', 10)
 
print(student_best.grades)
