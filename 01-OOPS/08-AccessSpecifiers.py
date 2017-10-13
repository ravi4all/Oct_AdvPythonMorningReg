class Emp:

    # _name = "Ram"
    # __salary = 15000

    def __init__(self):
        self.age = 20
        self._name = "Ram"
        self.__salary = 15000

    def printEmp(self):
        print(self._name,"is earning", self.__salary)

obj = Emp()
print(obj._name)
print(obj.age)
# print(obj.__salary)

obj.printEmp()
print(obj.__dict__)

# print(Emp._name)
# print(Emp.__salary)
# print(Emp.age)
