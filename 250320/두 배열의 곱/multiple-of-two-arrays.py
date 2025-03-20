import sys

data = sys.stdin.read().strip().split("\n")

inputList = [list(map(int, data[i].split())) for i in range(3)]

for i in range(3):
    iList = list(map(int, data[i + 4].split()))

    for j in range(3):
        inputList[i][j] *= iList[j]

for row in inputList:
    print(" ".join(map(str, row)))