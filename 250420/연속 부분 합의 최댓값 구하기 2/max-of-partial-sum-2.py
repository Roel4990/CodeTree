n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
answer = min(a)
first = 0
second = 0

while True:
    sumNum = sum(a[first:second+1])
    answer = max(answer, sumNum)
    if sumNum > 0:
        if second == len(a) - 1:
            break
        second += 1
    else:
        if first == second:
            if second == len(a) - 1:
                break
            first += 1
            second += 1
        else:
            first = second
print(answer)