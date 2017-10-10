Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Emp:
	print("My First Class...")

	
My First Class...
>>> Emp
<class '__main__.Emp'>
>>> Emp.__class__
<class 'type'>
>>> type(Emp)
<class 'type'>
>>> a = 12
>>> type(a)
<class 'int'>
>>> type(int)
<class 'type'>
>>> Emp()
<__main__.Emp object at 0x00000196E5847240>
>>> class Emp:
	id = 1
	name = "Ram"

	
>>> Emp
<class '__main__.Emp'>
>>> Emp.id
1
>>> Emp.name
'Ram'
>>> name
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> Emp.__dict__
mappingproxy({'__module__': '__main__', 'id': 1, 'name': 'Ram', '__dict__': <attribute '__dict__' of 'Emp' objects>, '__weakref__': <attribute '__weakref__' of 'Emp' objects>, '__doc__': None})
>>> class Emp:
	"""This is my first class"""
	id = 1
	name = "Ram"

	
>>> Emp.__dict__
mappingproxy({'__module__': '__main__', '__doc__': 'This is my first class', 'id': 1, 'name': 'Ram', '__dict__': <attribute '__dict__' of 'Emp' objects>, '__weakref__': <attribute '__weakref__' of 'Emp' objects>})
>>> Emp.__doc__
'This is my first class'
>>> Emp.__module__
'__main__'
>>> obj = Emp()
>>> obj
<__main__.Emp object at 0x00000196E57EECF8>
>>> type(obj)
<class '__main__.Emp'>
>>> isinstance(Emp, obj)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    isinstance(Emp, obj)
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> isinstance('Emp', obj)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    isinstance('Emp', obj)
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> isinstance(2, int)
True
>>> isinstance(obj, 'Emp')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    isinstance(obj, 'Emp')
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> isinstance(obj, Emp)
True
>>> obj_1 = obj
>>> obj_1
<__main__.Emp object at 0x00000196E57EECF8>
>>> obj
<__main__.Emp object at 0x00000196E57EECF8>
>>> obj.id
1
>>> obj_1.id
1
>>> obj_1.id = 2
>>> obj
<__main__.Emp object at 0x00000196E57EECF8>
>>> obj.id
2
>>> obj_1.id
2
>>> id(obj_1)
1747607022840
>>> id(obj)
1747607022840
>>> a = [45,21,56,'Hi','Hey',11]
>>> b = a
>>> a[0] = "Bye"
>>> a
['Bye', 21, 56, 'Hi', 'Hey', 11]
>>> b
['Bye', 21, 56, 'Hi', 'Hey', 11]
>>> c = a[:]
>>> c
['Bye', 21, 56, 'Hi', 'Hey', 11]
>>> a
['Bye', 21, 56, 'Hi', 'Hey', 11]
>>> a[0] = 'Python'
>>> a
['Python', 21, 56, 'Hi', 'Hey', 11]
>>> c
['Bye', 21, 56, 'Hi', 'Hey', 11]
>>> a[:]
['Python', 21, 56, 'Hi', 'Hey', 11]
>>> id(c)
1747607474696
>>> id(a)
1747607251208
>>> a = [45,21,56,'Hi','Hey',11, ['Hey','There','Python',11,12],100]
>>> d = a[:]
>>> a[6][0]
'Hey'
>>> a[6][0] = 99
>>> a
[45, 21, 56, 'Hi', 'Hey', 11, [99, 'There', 'Python', 11, 12], 100]
>>> d
[45, 21, 56, 'Hi', 'Hey', 11, [99, 'There', 'Python', 11, 12], 100]
>>> e = a.copy()
>>> e
[45, 21, 56, 'Hi', 'Hey', 11, [99, 'There', 'Python', 11, 12], 100]
>>> a[6][0] = 100
>>> a
[45, 21, 56, 'Hi', 'Hey', 11, [100, 'There', 'Python', 11, 12], 100]
>>> e
[45, 21, 56, 'Hi', 'Hey', 11, [100, 'There', 'Python', 11, 12], 100]
>>> import copy
>>> f = copy.deepcopy(a)
>>> f
[45, 21, 56, 'Hi', 'Hey', 11, [100, 'There', 'Python', 11, 12], 100]
>>> a[6][0] = 'Hey'
>>> f
[45, 21, 56, 'Hi', 'Hey', 11, [100, 'There', 'Python', 11, 12], 100]
>>> a
[45, 21, 56, 'Hi', 'Hey', 11, ['Hey', 'There', 'Python', 11, 12], 100]
>>> 
