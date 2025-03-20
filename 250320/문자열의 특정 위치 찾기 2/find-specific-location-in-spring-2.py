n = input()

strList = ["apple", "banana", "grape", "blueberry", "orange"]

cnt = 0
for i in strList:
    if i[2] == n or i[3] == n:
        cnt += 1
        print(i)
    
print(cnt)