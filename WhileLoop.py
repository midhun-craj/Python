# While Loop

# name = input("Enter your name: ")
# while name == "":
#     print("You didn't enter your name.")
#     name = input("Enter your name: ")
# print(f"Hi, {name}")

food = input("Enter the food(q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter the food(q to quit): ")
print("Bye")
