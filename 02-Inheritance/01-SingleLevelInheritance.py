class Car:

    def __init__(self):
        self.speed = 250
        self.color = "Blue"
        self.gearSystem = True

    def printCar(self):
        print("Car details :", self.speed, self.color, self.gearSystem)

    def show(self):
        print("This function will be overrided....")

class Audi(Car):

    def __init__(self, name,color):
        self.name = name
        super().__init__()
        self.color = color

    def show(self):
        super().show()
        print("I will execute...")


obj = Audi("Audi", "red")
obj.printCar()
obj.show()
