
try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Please enter a number")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some clean up here..")