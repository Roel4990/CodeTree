N = int(input())

resultNum = 0

for i in range(1, N+1):
    resultNum += i
    if resultNum >= N:
        print(i)
        break