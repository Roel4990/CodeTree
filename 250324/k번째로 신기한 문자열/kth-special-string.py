n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
existStr = []
for i in str:
    if i.startswith(t):
        existStr.append(i)
existStr.sort()
print(existStr[k-1])