N = int(input())
NList = list(map(int, input().split()))

print(*[x ** 2 for x in NList])