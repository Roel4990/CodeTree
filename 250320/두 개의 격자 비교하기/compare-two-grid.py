N, M = map(int, input().split())

resultList = [[0 for _ in range(M)] for _ in range(N)]

inputList = []

for i in range(N):
    inputList.append(list(map(int, input().split())))

for i in range(N):
    iList = list(map(int, input().split()))

    for j in range(M):
        if inputList[i][j] != iList[j]:
            resultList[i][j] = 1


for i in resultList:
    print(" ".join(map(str, i)))