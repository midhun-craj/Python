
# def add_numbers(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# print(add_numbers(1, 2, 3, 4, 5))

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
print_address(street = "123",
              city = "Kochi", pin = "123654")