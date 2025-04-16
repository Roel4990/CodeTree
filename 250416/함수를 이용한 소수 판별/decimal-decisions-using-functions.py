a, b = map(int, input().split())

# Please write your code here.

def f(a, b):
    answerList = []
    for i in range(a, b+1):
        isPrimeNumber = True
        for j in range(2, i):
            if i % j == 0:
                isPrimeNumber = False
        if isPrimeNumber: answerList.append(i)
    return answerList

print(sum(f(a, b)))