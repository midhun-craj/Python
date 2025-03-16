word = "apple"
user = input("Enter a letter? ")
# if user in word:
#     print(f"{user} in the word")
# else:
#     print("The letter is not in the word.")

if user not in word:
    print("The letter not in the word.")
else:
    print(f"{user} is in the word.")