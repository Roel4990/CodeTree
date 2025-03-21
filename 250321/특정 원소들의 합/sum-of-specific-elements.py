result = 0
for i in range(4):
    nList = list(map(int, input().split()))

    for j in range(i+1):
        result += nList[j]

print(result)