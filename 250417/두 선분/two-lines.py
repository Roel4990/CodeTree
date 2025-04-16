x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.

if (x3 <= x2 and x1 <= x4) or (x2 <= x3 and x4 <= x1):
    print('intersecting')
else:
    print("nonintersecting")

