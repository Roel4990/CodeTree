n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class Info:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

info1 = Info(name.pop(), street_address.pop(), region.pop())

print(f"name {info1.name}\naddr {info1.addr}\ncity {info1.city}")

