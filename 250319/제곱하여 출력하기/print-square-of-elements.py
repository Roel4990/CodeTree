N = int(input())
NList = list(map(int, input().split()))

print("".join(x ** 2 for x in NList))