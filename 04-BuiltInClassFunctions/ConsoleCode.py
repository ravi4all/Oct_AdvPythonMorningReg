Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Car:
	def __init__(self,name,color):
		self.name = name
		self.color = color

	
>>> obj = Car('Audi', 'RED')
>>> print(obj)
<__main__.Car object at 0x00000269D71F61D0>
>>> str(obj)
'<__main__.Car object at 0x00000269D71F61D0>'
>>> class Car:
	def __init__(self,name,color):
		self.name = name
		self.color = color
	def __str__(self):
		return self.name + " " + self.color

	
>>> obj = Car('Audi', 'RED')
>>> obj
<__main__.Car object at 0x00000269D723AE80>
>>> print(obj)
Audi RED
>>> class Car:
	def __init__(self,name,color):
		self.name = name
		self.color = color
	def __str__(self):
		return self.name + " " + self.color
	def __repr__(self):
		return self.name + " " + self.color

	
>>> obj = Car('Audi', 'RED')
>>> obj
Audi RED
>>> print(obj)
Audi RED
>>> import date
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    import date
ModuleNotFoundError: No module named 'date'
>>> import datetime
>>> datetime.date.today()
datetime.date(2017, 10, 18)
>>> today = datetime.date.today()
>>> str(today)
'2017-10-18'
>>> repr(today)
'datetime.date(2017, 10, 18)'
>>> print(today)
2017-10-18
>>> 
