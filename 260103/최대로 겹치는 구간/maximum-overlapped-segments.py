n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
maxNum = -101
minNum = 101

for a, b in segments:
    if a < minNum:
        minNum = a
    if b > maxNum:
        maxNum = b

lineList = [0 for i in range(minNum, maxNum + 1)]

for a, b in segments:
    for i in range(a, b):
        lineList[i-1] += 1

print(max(lineList))