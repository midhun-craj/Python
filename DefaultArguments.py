# def net_price(price, discount = .1, tax = 0.05):
#     return f"${price * (1 - discount) * (1 + tax)}"

# print(net_price(150))

import time

def count(end, start = 0):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("done")

count(10)