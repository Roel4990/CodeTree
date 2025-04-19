nList = list(map(int, input().split()))

def f(nList):
    if len(nList) == 10:
        return nList
    num = nList[-1] + nList[-2] * 2
    nList.append(num)
    return f(nList)

print(" ".join(map(str, f(nList))))