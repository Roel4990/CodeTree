n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.
class Info:
    def __init__(self, height, weight, idx):
        self.height = height
        self.weight = weight
        self.idx = idx

studentInfos = [Info(student[0], student[1], student[2]) for student in students]

studentInfos.sort(key = lambda x: (-x.height, -x.weight, x.idx))

for studentInfo in studentInfos:
    print(studentInfo.height, studentInfo.weight, studentInfo.idx)