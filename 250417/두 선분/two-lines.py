x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.

if x1 <= x3 <= x2:
    print("intersecting")
elif x3 <= x2 <= x4:
    print("intersecting")
else:
    print("nonintersecting")
    