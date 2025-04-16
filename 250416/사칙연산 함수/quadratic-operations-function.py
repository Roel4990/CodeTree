a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
match o:
    case "+":
        print(a, o, c, "=", a+c, sep=" ")
    case "-":
        print(a, o, c, "=", a-c, sep=" ")
    case "/":
        print(a, o, c, "=", a/c, sep=" ")
    case "*":
        print(a, o, c, "=", a*c, sep=" ")
    case _:
        print(False)