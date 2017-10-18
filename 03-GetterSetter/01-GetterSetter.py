# Descriptors - Getters and Setters
class Person:

    def __init__(self):
        self.__name = ""

    def __set__(self, instance, value):
        self.__name = value
        print("Setting {}".format(self.__name))
        print(instance, value)

    def __get__(self, instance, owner):
        print("Getting {}".format(self.__name))
        print(instance, owner)
        return self.__name

    def __delete__(self, instance):
        print("Deleting {}".format(self.__name))

class Emp:
    userName = Person()

obj = Emp()
obj.userName = "Ram"
obj.userName
del obj.userName
