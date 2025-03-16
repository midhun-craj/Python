class Animal:
    def __init__(self, name):
        self.name = name

    def naming(self):
        print(f"The animal name is {self.name}")

class Dog(Animal):
    
    def naming(self):
        print(f"The dog name is {self.name}")

class Cat(Animal):
    pass  


dog = Dog("Husky")
dog.naming()

cat = Cat("Bush")
cat.naming()