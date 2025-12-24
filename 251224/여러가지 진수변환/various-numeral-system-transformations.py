N, B = map(int, input().split())

# Please write your code here.
resultList= []
while True:
    if N == 0:
        break;
    a = N%B
    N //= B
    resultList.append(a)
resultList.reverse()
print("".join(map(str, resultList)))