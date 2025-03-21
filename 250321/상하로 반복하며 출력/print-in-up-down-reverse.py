n = int(input())

nList = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            nList[j][i] = j+1
    else:
        for j in range(n-1, -1, -1):
            nList[j][i] = n - j

for i in nList:
    print("".join(map(str, i)))
        
