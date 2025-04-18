n = int(input())

def stars(N):
    if N == 0:
        return
    print('* ' * N)
    stars(N-1)
    print('* ' * N)

stars(n)