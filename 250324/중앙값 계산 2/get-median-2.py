n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
resultList = []
for i in range(len(arr)):
    if i % 2 == 0:
        checkList = arr[:i+1]
        checkList.sort()
        resultList.append(checkList[i//2])

print(" ".join(map(str, resultList)))
    