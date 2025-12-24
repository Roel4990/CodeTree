binary = input()

# Please write your code here.
n = len(binary)
binary = list(map(int, binary))
num = 0

for i in range(n):
    num = num * 2 + binary[i]

print(num)
