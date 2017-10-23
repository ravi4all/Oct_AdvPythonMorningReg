Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> data = "Hello world, this is python regex"
>>> re.match('[A-Z]', data)
<_sre.SRE_Match object; span=(0, 1), match='H'>
>>> re.match('[a-z]', data)
>>> re.match('[a-z]\w', data)
>>> re.match('/[a-z]+', data)
>>> re.match('/[a-z]\w+', data)
>>> re.search('/[a-z]\w+', data)
>>> re.search('[a-z]', data)
<_sre.SRE_Match object; span=(1, 2), match='e'>
>>> re.findall('[a-z]', data)
['e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 't', 'h', 'i', 's', 'i', 's', 'p', 'y', 't', 'h', 'o', 'n', 'r', 'e', 'g', 'e', 'x']
>>> re.search('[a-z]+', data)
<_sre.SRE_Match object; span=(1, 5), match='ello'>
>>> re.search('[a-z]\w+', data)
<_sre.SRE_Match object; span=(1, 5), match='ello'>
>>> re.search('\w+', data)
<_sre.SRE_Match object; span=(0, 5), match='Hello'>
>>> re.search('\s+', data)
<_sre.SRE_Match object; span=(5, 6), match=' '>
>>> re.search('\w', data)
<_sre.SRE_Match object; span=(0, 1), match='H'>
>>> re.findall('[a-z]\w+', data)
['ello', 'world', 'this', 'is', 'python', 'regex']
>>> re.findall('[A-Z a-z]\w+', data)
['Hello', ' world', ' this', ' is', ' python', ' regex']
>>> data_1 = "Salary of Ram is 15000, Salary of Shyam is 18000"
>>> re.findall('[A-Z 0-9]\w+', data)
['Hello', ' world', ' this', ' is', ' python', ' regex']
>>> re.findall('[A-Z 0-9]\w+', data_1)
['Salary', ' of', ' Ram', ' is', ' 15000', ' Salary', ' of', ' Shyam', ' is', ' 18000']
>>> re.findall('[A-Z0-9]\w+', data_1)
['Salary', 'Ram', '15000', 'Salary', 'Shyam', '18000']
>>> data_2 = "id of ram is ram123@gmail.com and id of shyam is shyam.11_22@gmail.com and they will meet @ 11:00 am"
>>> re.findall('[a-z0-9]@[\w+.]', data_1)
[]
>>> re.findall('[a-z0-9]@[\w+.]', data_2)
['3@g', '2@g']
>>> re.findall('[a-z0-9]@[.]\w+', data_2)
[]
>>> re.findall('[a-z0-9]@[_.]\w+', data_2)
[]
>>> re.findall('[a-z0-9]@[-.]\w+', data_2)
[]
>>> re.findall('[a-z0-9][_.]@[a-z][.]\w+', data_2)
[]
>>> re.findall('[a-z0-9]\w+', data_2)
['id', 'of', 'ram', 'is', 'ram123', 'gmail', 'com', 'and', 'id', 'of', 'shyam', 'is', 'shyam', '11_22', 'gmail', 'com', 'and', 'they', 'will', 'meet', '11', '00', 'am']
>>> re.findall('[a-z0-9][@]\w+', data_2)
['3@gmail', '2@gmail']
>>> re.findall('/[a-z0-9][@]\w+', data_2)
[]
>>> re.findall('[a-z|0-9][@]\w+', data_2)
['3@gmail', '2@gmail']
>>> re.findall('[a-z][@]\w+', data_2)
[]
>>> re.findall('[a-z]\w+', data_2)
['id', 'of', 'ram', 'is', 'ram123', 'gmail', 'com', 'and', 'id', 'of', 'shyam', 'is', 'shyam', 'gmail', 'com', 'and', 'they', 'will', 'meet', 'am']
>>> re.findall('[a-z][0-9]@\w+', data_2)
[]
>>> re.findall('[0-9]@[a-z]\w+', data_2)
['3@gmail', '2@gmail']
>>> re.findall('[a-z0-9]@[a-z]\w+', data_2)
['3@gmail', '2@gmail']
>>> re.findall('[a-z]\w+[0-9]@[a-z]\w+', data_2)
['ram123@gmail']
>>> re.findall('[a-z]\w+[0-9]@[a-z.]\w+', data_2)
['ram123@gmail']
>>> re.findall('[a-z]\w+[0-9]@[a-z][.]\w+', data_2)
[]
>>> re.findall('[a-z]\w+[0-9]@[a-z]+[.]\w+', data_2)
['ram123@gmail.com']
>>> re.findall('[a-z]\w+[0-9]+[._]+@[a-z]+[.]\w+', data_2)
[]
>>> re.findall('[a-z]\w+|[0-9]+ |[._]+@[a-z]+[.]\w+', data_2)
['id', 'of', 'ram', 'is', 'ram123', 'gmail', 'com', 'and', 'id', 'of', 'shyam', 'is', 'shyam', 'gmail', 'com', 'and', 'they', 'will', 'meet', '00 ', 'am']
>>> re.findall('[a-z]\w+[0-9]+|[._]+@[a-z]+[.]\w+', data_2)
['ram123']
>>> re.findall('[a-z]\w+[0-9]\w+[._]+@[a-z]+[.]\w+', data_2)
[]
>>> re.findall('[a-z]\w+[0-9]\w+@[a-z]+[.]\w+', data_2)
['ram123@gmail.com']
>>> re.findall('[a-z]|[._]\w+[0-9]\w+@[a-z]+[.]\w+', data_2)
['i', 'd', 'o', 'f', 'r', 'a', 'm', 'i', 's', 'r', 'a', 'm', 'g', 'm', 'a', 'i', 'l', 'c', 'o', 'm', 'a', 'n', 'd', 'i', 'd', 'o', 'f', 's', 'h', 'y', 'a', 'm', 'i', 's', 's', 'h', 'y', 'a', 'm', '.11_22@gmail.com', 'a', 'n', 'd', 't', 'h', 'e', 'y', 'w', 'i', 'l', 'l', 'm', 'e', 'e', 't', 'a', 'm']
>>> re.findall('[a-z][._]\w+[0-9]\w+@[a-z]+[.]\w+', data_2)
['m.11_22@gmail.com']
>>> re.findall('[a-z]+[._]+[0-9]+@[a-z]+[.]\w+', data_2)
[]
>>> re.findall('[\w.-]+@+[\w.-]+', data_2)
['ram123@gmail.com', 'shyam.11_22@gmail.com']
>>> re.findall('[\w.]+@+[\w.]+', data_2)
['ram123@gmail.com', 'shyam.11_22@gmail.com']
>>> re.findall('[\w]+@+[\w]+', data_2)
['ram123@gmail', '11_22@gmail']
>>> re.findall('[\w.]+@+[\w.]+', data_2)
['ram123@gmail.com', 'shyam.11_22@gmail.com']
>>> 
