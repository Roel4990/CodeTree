numList = []
def f(n):
    return format(n, '.1f')
for _ in range(2):
    nList = list(map(int, input().split()))
    numList.append(nList)
    print(f(sum(nList)/len(nList)), end=" ")
print()
for i in range(4):
    print(f((numList[0][i] + numList[1][i])/len(numList)), end=" ")
print()
print(f((sum(numList[0]) + sum(numList[1]))/(len(numList[0]) + len(numList[1]))))

