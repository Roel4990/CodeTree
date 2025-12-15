n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
class Student:
    def __init__(self, height, weight, idx):
        self.height = height
        self.weight = weight
        self.idx = idx

students = [Student(student[0], student[1], student[2]) for student in students]

students.sort(key = lambda x: (x.height, -x.weight))

for student in students:
    print(student.height, student.weight, student.idx)