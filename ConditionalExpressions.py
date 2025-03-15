# Conditional Expressions

# num = 1
# print("Positive" if num > 0 else "Negative")

# a = 1
# b = 2
# max_num = a if a > b else b
# min_num = a if a < b else b
# print(min_num)
# print(max_num)

user_role = "admin"
access = "full access" if user_role == "admin" else "limited access"
print(access)