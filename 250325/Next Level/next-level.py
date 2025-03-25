user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class user:
    def __init__(self, user_id, user_level):
        self.user_id = user_id
        self.user_level = user_level

user1 = user("codetree", 10)
user2 = user(user2_id, user2_level)

print(f"user {user1.user_id} lv {user1.user_level}")
print(f"user {user2.user_id} lv {user2.user_level}")