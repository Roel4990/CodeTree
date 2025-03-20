N = input()
N = list(N)
N[1] = "a"
N[-2] = "a"
N = "".join(N)
print(N)