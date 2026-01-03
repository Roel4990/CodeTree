n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
maxNum = -101
minNum = 101

for a, b in segments:
    minNum = min(minNum, a)
    maxNum = max(maxNum, b)

lineList = [0] * (maxNum - minNum + 1)

for a, b in segments:
    for i in range(a, b):
        lineList[i - minNum] += 1

print(max(lineList))