class Emp:
    """This is my first class"""
    id = 101
    name = 'Ram'
    age = 21

obj = Emp()
print(obj)
print(obj.id, obj.name, obj.age)
print(obj.__doc__)
print(obj.__module__)
print(obj.__dict__)
print(obj.__class__)

# x = 0x000001979D9D8710
# print(x)
# print(type(x))
