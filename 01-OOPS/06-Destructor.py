class Emp:

    def __init__(self):
        self.name = "Ram"
        self.age = 20

    def __del__(self):
        print(__class__.__name__ , "destroyed")

obj = Emp()
obj_1 = obj

# del obj

print(obj_1.name)
print(obj.name)
