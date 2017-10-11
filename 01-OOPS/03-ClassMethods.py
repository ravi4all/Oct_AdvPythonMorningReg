class Emp:
    id = 0
    name = None
    age = 0

    def printEmp(self):
        # print(Emp.id, Emp.name, Emp.age)
        # self.id = 101
        # self.name = 'John'
        print(self.id, self.name,self.age)


obj = Emp()
obj.id = 1
obj.name = "Ram"
obj.age = 20
obj.printEmp()

obj_1 = Emp()
obj_1.id = 2
obj_1.name = "Shyam"
obj_1.age = 22
obj_1.printEmp()

