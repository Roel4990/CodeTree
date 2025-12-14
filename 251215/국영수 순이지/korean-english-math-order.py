n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
class Grade:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

grades = [Grade(grade[0], grade[1], grade[2], grade[3]) for grade in zip(name, korean, english, math)]

grades.sort(key=lambda x : (-x.kor, -x.eng,-x.math))

for grade in grades:
    print(grade.name, grade.kor, grade.eng, grade.math)