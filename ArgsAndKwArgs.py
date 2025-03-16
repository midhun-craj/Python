
# def add_numbers(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# print(add_numbers(1, 2, 3, 4, 5))

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
    
# print_address(street = "123",
#               city = "Kochi", pin = "123654")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}") 

shipping_label("Eng. ", "Midhun ", "C Raj", 
            #    apt = "123 Fake street",
            street = "vv",
               pobox = "PO box ",
               city = "Kollam",
               state = "Kerala",
               zip = "123456")   