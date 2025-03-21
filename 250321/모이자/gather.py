n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
import sys
min_val = sys.maxsize
for i in range(5):
    move = 0
    for j in range(-i,n-i):
        move += A[j+i]*abs(j)
    min_val = min(move, min_val)

print(min_val)
