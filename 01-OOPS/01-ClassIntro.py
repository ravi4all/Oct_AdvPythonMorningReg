class Emp:
    """This is my first class demo"""
    id = 1
    name = "Ram"
    print("Hello world")

print(Emp.id, Emp.name)

if __name__ == '__main__':
    print(Emp.__dict__)
    print(Emp.__module__)
    print(Emp.__doc__)
