n = int(input())

# Please write your code here.
# for i in range(n, -n-1, -1):
#     if i == 0: continue
#     print("* " * abs(i))

def stars(N):
    if N == 0:
        return
    print('* ' * N)
    stars(N-1)
    print('* ' * N)

stars(n)