# start, end = map(int, input().split())

# # Please write your code here.
N = int(input())

start = 1

for i in range(1, N+1):
    for j in range(i):
        print(start, end=" ")
        start += 1
    print()