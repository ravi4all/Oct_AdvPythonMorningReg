data = {"id" : 101, "name" : "Ram", "age" : 20}

class Emp:
    print("This is emp class")

    def __str__(self):
        return " "

obj = Emp()

with open("demo.txt", 'w') as file:
    file.write(str(obj))
