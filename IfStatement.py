# If Statement

age = int(input("Enter your age? "))
if(age > 100):
    print("You're now signed up!")
elif(age <= 0):
    print("You are not even born yet")
elif(age >= 18):
    print("You are too old to sign up")
else:
    print("You must be 18+ to sign up")