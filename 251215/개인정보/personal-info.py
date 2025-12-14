n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.

class Info:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = [Info(person[0], person[1], person[2]) for person in zip(name, height, weight)]

people.sort(key = lambda x: x.name)

print("name")
for person in people:
    print(person.name, person.height, person.weight)

people.sort(key = lambda x: -x.height)

print("\nheight")
for person in people:
    print(person.name, person.height, person.weight)