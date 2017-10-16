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
        super().__init__()
        self.name = name
        self.color = color

    def show(self):
        super().show()
        print("I will execute...")

class Audi_2(Audi):

    def __init__(self, name,color, speed):
        self.name = name
        self.color = color
        super().__init__(self.name, self.color)
        self.speed = speed


obj = Audi_2("Audi", "silver", 300)
obj.printCar()
obj.show()
