N = input()

# Please write your code here.
n = len(N)
binary = list(map(int, N))
num = 0

for i in range(n):
    num = num * 2 + binary[i]

num *= 17
resultList=[]
while True:
    if num == 0:
        break
    a = num%2
    num //= 2
    resultList.append(a)

resultList.reverse()

print("".join(map(str, resultList)))