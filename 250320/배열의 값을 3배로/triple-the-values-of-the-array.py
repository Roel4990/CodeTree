inputList = []
for _ in range(3):
    inputList.append(list(map(int, input().split())))

for i in range(3):
    for j in range(3):
        inputList[i][j] *= 3

for i in inputList:
    print(" ".join(map(str, i))) 