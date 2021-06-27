class Grade:
    def __init__(self, start, to, gradeName):
        self.start = start
        self.to = to
        self.gradeName = gradeName


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


def two_sum_problem(arr, target):
    differences = {}
    for i, val in enumerate(arr):
        if val in differences:
            return differences[val], i
        else:
            differences[target - val] = i


def grade_student(marks, grds):
    for grade in grds:
        if grade.start <= marks <= grade.to:
            return grade.gradeName
    raise ValueError("Wrong marks")


def super_students(grds, students):
    grade_A_B_studs = []
    for student in students:
        marks = student.marks
        if grade_student(marks, grds) in ['A', 'B']:
            grade_A_B_studs.append(student.name)
    return grade_A_B_studs


if __name__ == "__main__":
    print(two_sum_problem([2, 7, 11, 15], 9))

    print(two_sum_problem([3, 2, 4], 6))

    print(two_sum_problem([3, 3], 6))

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
    super_students(grades, students)
