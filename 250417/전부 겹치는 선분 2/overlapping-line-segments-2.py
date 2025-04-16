n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

# Please write your code here.
isPossible = False
x1List = x1[:]
x2List = x2[:]
for i in range(n):
    x1List.pop(i)
    x2List.pop(i)
    if max(x1List) <= min(x2List):
        isPossible = True
    x1List = x1[:]
    x2List = x2[:]

print("Yes" if isPossible else "No")