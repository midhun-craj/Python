
class Cars:
    
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

    def drive(self):
        print(f"You drive a {self.year} model {self.color} color {self.name}")

        