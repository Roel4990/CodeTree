numList = list(map(int, input().split()))
for i in range(len(numList)):
    if numList[i] % 3 == 0:
        print(numList[i-1])
        break