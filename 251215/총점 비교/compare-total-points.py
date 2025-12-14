n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.
class Grade:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

grades = [Grade(grade[0], grade[1], grade[2], grade[3]) for grade in zip(name, score1, score2, score3)]

grades.sort(key=lambda x: x.kor + x.eng + x.math)

for grade in grades:
    print(grade.name, grade.kor, grade.eng, grade.math)
