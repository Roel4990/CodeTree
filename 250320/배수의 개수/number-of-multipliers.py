nList = []
for _ in range(10):
    nList.append(int(input()))

threeCnt = 0
fiveCnt = 0

for i in nList:
    if i % 3 == 0:
        threeCnt += 1
    if i % 5 == 0:
        fiveCnt += 1

print(threeCnt, fiveCnt, sep=" ")