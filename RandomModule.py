import random

# print(random.randint(1, 10))
# print(random.choice(("rock", "paper", "scissors")))
# print(random.random())
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
random.shuffle(cards)
print(cards)