x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.

if ((a1 <= x2 and x1 <= a2) or (x2 <= a1 and a2 <= x1)) and ((b1 <= y2 and y1 <= b2) or (y2 <= b1 and b2 <= y1)):
    print("overlapping")
else:
    print("nonoverlapping")

