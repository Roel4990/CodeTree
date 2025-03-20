N = int(input())
nList = list(map(int, input().split()))

resultList = []

for i in nList:
    if i % 2 == 0:
        resultList.append(i)

print(" ".join(map(str, resultList[::-1])))