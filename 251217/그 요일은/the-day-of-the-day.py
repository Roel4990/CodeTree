m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
day_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

day_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = 0
result = 0
if m1 == m2 and d1 == d2:
    print(0)
else:
    for i in range(m1, m2):
        day = d1
        if i == m1:
            count += day_of_month[i] - d1
        else:
            count += day_of_month[i]

    count += d2

    a = day_of_the_week.index(A)

    print(count//7 + (1 if count % 7 >= a else 0))