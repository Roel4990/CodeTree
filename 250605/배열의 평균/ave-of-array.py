numList = []

for _ in range(2):
    nList = list(map(int, input().split()))
    numList.append(nList)
    print(sum(nList)/len(nList), end=" ")
print()
for i in range(4):
    print((numList[0][i] + numList[1][i])/len(numList), end=" ")
print()
print((sum(numList[0]) + sum(numList[1]))/(len(numList[0]) + len(numList[1])))

