Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list1 = ["apple", 10, 3.14, [1, 2, 3], "class", 20, [4.5, 6.7], 5.5]

list2 = [8, "list in python", [9.1, 7.2], 15, "MAC", [2, 4, 6], 3.33, 12.5]

list1[2][1]

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    list1[2][1]
TypeError: 'float' object is not subscriptable
list2[3][0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list2[3][0]
TypeError: 'int' object is not subscriptable
list1[4][2][1]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list1[4][2][1]
IndexError: string index out of range
len(list2)
8
list1[12]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list1[12]
IndexError: list index out of range
list2[-4:-1]
['MAC', [2, 4, 6], 3.33]
list1[2:14]
[3.14, [1, 2, 3], 'class', 20, [4.5, 6.7], 5.5]
list2+list1
[8, 'list in python', [9.1, 7.2], 15, 'MAC', [2, 4, 6], 3.33, 12.5, 'apple', 10, 3.14, [1, 2, 3], 'class', 20, [4.5, 6.7], 5.5]
list1*2
['apple', 10, 3.14, [1, 2, 3], 'class', 20, [4.5, 6.7], 5.5, 'apple', 10, 3.14, [1, 2, 3], 'class', 20, [4.5, 6.7], 5.5]
list2[5][1] = 0
list2
[8, 'list in python', [9.1, 7.2], 15, 'MAC', [2, 0, 6], 3.33, 12.5]
del list1[-3]
list1
['apple', 10, 3.14, [1, 2, 3], 'class', [4.5, 6.7], 5.5]
list1.append('university')
list1
['apple', 10, 3.14, [1, 2, 3], 'class', [4.5, 6.7], 5.5, 'university']
list2
[8, 'list in python', [9.1, 7.2], 15, 'MAC', [2, 0, 6], 3.33, 12.5]
list2.pop()
12.5
list2
[8, 'list in python', [9.1, 7.2], 15, 'MAC', [2, 0, 6], 3.33]
list1
['apple', 10, 3.14, [1, 2, 3], 'class', [4.5, 6.7], 5.5, 'university']
list1.insert(5,100)
list1
['apple', 10, 3.14, [1, 2, 3], 'class', 100, [4.5, 6.7], 5.5, 'university']
list2
[8, 'list in python', [9.1, 7.2], 15, 'MAC', [2, 0, 6], 3.33]
list2.extend([44, 50])
list2
[8, 'list in python', [9.1, 7.2], 15, 'MAC', [2, 0, 6], 3.33, 44, 50]
str1 = "Django allows a rapid web development and creates scalable systems"

str2 = "There are two areas in cloud computing: performance and security"

str2[-1:-6:-1]

'ytiru'
str1[9]

'l'
str2[-2:]

'ty'
str2[0:20:3]

'Tra ors'
s1+" "+s2

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s1+" "+s2
NameError: name 's1' is not defined
str1.endswith('systems')
True
str2.split()

['There', 'are', 'two', 'areas', 'in', 'cloud', 'computing:', 'performance', 'and', 'security']
str1.upper(), str2.upper()

('DJANGO ALLOWS A RAPID WEB DEVELOPMENT AND CREATES SCALABLE SYSTEMS', 'THERE ARE TWO AREAS IN CLOUD COMPUTING: PERFORMANCE AND SECURITY')
str1.replace('web', '')
'Django allows a rapid  development and creates scalable systems'
str2.count('e')

7
d1={"name": "Bob", "age": 35, (4, 10):['x', 'y', 'z'], '+1' : "Canada", 44: 99, 19:555}

d2 = dict([("name","Livy"), ('age', 44), ((1, 3, 5), ['a', 'b', 'c']), (0, 'black'), (33, 67)])

d3 = dict(id=2277, name='Michael', siblings=['Janet', 'Martin', 'Richard'])

d1.keys()

dict_keys(['name', 'age', (4, 10), '+1', 44, 19])
d2.values()

dict_values(['Livy', 44, ['a', 'b', 'c'], 'black', 67])
d3.get('id')

2277
d2.get('age')

44
d3.get('age')

d3.get('name', 'Tim')

'Michael'
d2.items()
dict_items([('name', 'Livy'), ('age', 44), ((1, 3, 5), ['a', 'b', 'c']), (0, 'black'), (33, 67)])
d3['siblings']
['Janet', 'Martin', 'Richard']
d2['siblings']
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    d2['siblings']
KeyError: 'siblings'
d2.update(d3)
d2
{'name': 'Michael', 'age': 44, (1, 3, 5): ['a', 'b', 'c'], 0: 'black', 33: 67, 'id': 2277, 'siblings': ['Janet', 'Martin', 'Richard']}
d2[0]
'black'
d1.get((1,2))
d1
{'name': 'Bob', 'age': 35, (4, 10): ['x', 'y', 'z'], '+1': 'Canada', 44: 99, 19: 555}
d2['siblings']
['Janet', 'Martin', 'Richard']
d2['name']
'Michael'
d1 == d2
False
len(d2)
7
for key in d1.keys():
    print(key)

name
age
(4, 10)
+1
44
19
>>> for key in d2.keys():
...     print(d2[key])
... 
...     
Michael
44
['a', 'b', 'c']
black
67
2277
['Janet', 'Martin', 'Richard']
>>> str1 = "Django allows a rapid web development and creates scalable systems"
... 
... str2 = "There are two areas in cloud computing: performance and security"
... 
SyntaxError: multiple statements found while compiling a single statement
>>> str1+ "" +str2
'Django allows a rapid web development and creates scalable systemsThere are two areas in cloud computing: performance and security'
>>> str1+" "+str2
'Django allows a rapid web development and creates scalable systems There are two areas in cloud computing: performance and security'
>>> d1.get((0,0))
>>> d1.get(0,0)
0
>>> d1
{'name': 'Bob', 'age': 35, (4, 10): ['x', 'y', 'z'], '+1': 'Canada', 44: 99, 19: 555}
>>> d1.get('+1','+1')
'Canada'
>>> 
>>> d1.get('+1',44)
'Canada'
>>> d1.get(44,'+1')
99
>>> d1.get('+145','+1')
'+1'
>>> d1.get('+1455',+1)
1
