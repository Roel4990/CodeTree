a, b, c = map(int, input().split())

# Please write your code here.
if a - 11 < 0:
    print(-1)
else:
    print((a - 11 - 1) * 24 * 60 + (b + 23 - 11) * 60 + 60 + c - 11)