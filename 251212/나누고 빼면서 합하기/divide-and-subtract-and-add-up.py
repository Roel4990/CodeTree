n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
indexList = [m]
result = 0
while m != 1:
    if m % 2 == 0:
        m //= 2
    else:
        m -= 1
    indexList.append(m)

for i in indexList:
    result += A[i-1]

print(result)