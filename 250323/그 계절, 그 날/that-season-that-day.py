Y, M, D = map(int, input().split())

# Please write your code here.
def isYoon(Year):
    if Y % 4 == 0:
        if Y % 100 == 0 and Y % 400 != 0:
            return False
        else:
            return True
    else: 
        return False

def isExistDate(Year, Month, Day):
    if Month <= 7:
        if Month % 2 == 1:
            if Day <= 31: return True 
            else: return False 
        else:
            if Month == 2:
                dayNum = 29 if isYoon(Year) else 28
                if Day <= dayNum: return True 
                else: return False 
            else:
                if Day <= 30: return True 
                else: return False 
    elif Month <= 12:
        if Month % 2 == 0:
            if Day <= 31: return True 
            else: return False 
        else:
            if Day <= 30: return True 
            else: return False 
    else:
        return False

def weather(Month):
    if Month >= 3 and Month <=5:
        return "Spring"
    elif Month >= 6 and Month <=8:
        return "Summer"
    elif Month >= 9 and Month <=11:
        return "Fall"
    else:
        return "Winter"

print(weather(M) if isExistDate(Y, M, D) else -1)