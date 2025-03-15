# 2D Collection

groceries = (("apple", "orange", "banana"),
             ("celery", "oninion", "bitterguard"),
             ("chicken", "fish", "meat"))
# print(groceries)
for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()