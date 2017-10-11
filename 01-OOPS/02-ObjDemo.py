class Emp:
    """This is my first class demo"""
    id = 1
    name = "Ram"
    print("Hello world")


if __name__ == '__main__':
    obj_1 = Emp()
    # print(ram)
    print(obj_1.id, obj_1.name)
    obj_1.name = 'Shyam'
    print(obj_1.name)
    print(Emp.name)

    obj_2 = Emp()
    obj_2.name = 'Ram'
    obj_2.id = 2
    print(obj_2.id, obj_2.name)

    print("Id before changing...",Emp.id)
    Emp.id = 5
    print("Id after change",Emp.id)

    obj_3 = Emp()
    print(obj_3.id, obj_3.name)
