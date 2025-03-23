n = int(input())

# Please write your code here.

for i in range(n, -n-1, -1):
    if i == 0: continue
    print("* " * abs(i))
