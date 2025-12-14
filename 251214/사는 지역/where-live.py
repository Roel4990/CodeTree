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

max_name = max(name)

max_index = name.index(max_name)


info1 = Info(name[max_index], street_address[max_index], region[max_index])

print(f"name {info1.name}\naddr {info1.addr}\ncity {info1.city}")

