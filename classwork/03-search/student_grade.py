class Grade:
    def __init__(self, start, to, gradeName):
        self.start = start
        self.to = to
        self.gradeName = gradeName


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


grades = [
    Grade(90, 100, "A"),
    Grade(80, 89, "B"),
    Grade(70, 79, "C"),
    Grade(60, 69, "D"),
    Grade(0, 59, "E")
]

students = [
    Student("Dennis", 44),
    Student("Ken", 90),
    Student("Derick", 32),
    Student("James", 67),
    Student("Joyce", 76),
    Student("Linet", 29),
    Student("Ben", 96),
    Student("Jane", 82)
]

def grade_student(marks, grades):
    '''
    returns grade of student
    '''
    for grade in grades:
        if marks >= grade.start and marks <= grade.to:
            return grade.gradeName

    return "invalid: not within grading range"
    
# returns names of students who score grades A and B
def super_students(grades, students):

    ab_students = []

    for student in students:
        grade = grade_student(student.marks, grades)

        if grade == 'A' or grade == 'B':
            ab_students.append(student.name)

    return ab_students

# binary search
def grade_student_bs(marks, grades):
    l = 0
    r = len(grades)

    mid = l + (r-l)//2
    if grades[mid].start <= marks and grades[mid].to >= marks:
        return grades[mid].gradeName
    elif grades[mid].start < marks:
        r = mid
    elif grades[mid].to > marks:
        l = mid + 1
    return grade_student_bs(marks, grades[l:r])


def super_students_bs(grades, students):

    ab_students = []

    for student in students:
        
        grade = grade_student_bs(student.marks, grades)

        if grade == 'A' or grade == 'B':
            ab_students.append(student.name)

    return ab_students

print(super_students(grades, students))
# binary search recursive
print(super_students_bs(grades, students))
