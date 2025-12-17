m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

day_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = 0
a, b = d1, d2

for i in range(1, m1):
    a += day_of_month[i]
for i in range(1, m2):
    b += day_of_month[i]

print(day_of_the_week[(b - a)%7])