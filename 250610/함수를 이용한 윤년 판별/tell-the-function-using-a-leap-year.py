y = int(input())

# Please write your code here.

def isYoonYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else: 
            return True
    else:
        return False

print("true" if isYoonYear(y) else "false")