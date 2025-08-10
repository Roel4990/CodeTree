n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
found = any(a[i:i+n2] == b for i in range(n1 - n2 + 1))
print("Yes" if found else "No")