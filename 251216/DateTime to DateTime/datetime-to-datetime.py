a, b, c = map(int, input().split())

# Please write your code here.
result = 0
day = 11
hour = 11
minute = 11
while True:
    if day == a and hour == b and minute == c:
        break

    result += 1
    minute += 1

    if minute == 60:
        hour += 1
        minute = 0
    
    if hour == 24:
        day += 1
        hour = 0
print(result)