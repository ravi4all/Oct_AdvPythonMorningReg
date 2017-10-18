class Car:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return self.name + " " + self.color


audi = Car("Audi","red")
print(audi)
