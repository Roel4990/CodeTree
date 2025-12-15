n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
class Point:
    def __init__(self, idx, x, y, distance):
        self.idx = idx
        self.x = x
        self.y = y
        self.distance = distance

points_c = [Point(point[0], point[1][0], point[1][1], abs(point[1][0]) + abs(point[1][1])) for point in points]

points_c.sort(key = lambda x: x.distance)

for point in points_c:
    print(point.idx + 1)