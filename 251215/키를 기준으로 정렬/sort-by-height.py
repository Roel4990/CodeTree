n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
class Info:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = [Info(i[0], i[1], i[2]) for i in zip(name, height, weight)]

people.sort(lambda x: x.height)

for i in people:
    print(i.name, i.height, i.weight)
