# Logical Operators

# temp = 30
# is_raining = False

# if temp >= 35 or temp < 0 or is_raining:
#     print("Outdoor events are cancelled.")
# else:
#     print("The outdoor events are still scheduled.")

temp = -1
is_sunny = False

if temp > 28 and is_sunny:
    print("It's hot outside and sunny.")
elif 0 < temp < 28 and is_sunny:
    print("It's warm outside and its sunny.")
elif temp < 0 and not is_sunny:
    print("It's cold outside and it's sunny.")
else:
    print("The weather is unpredicatble.")
