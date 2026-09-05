Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
student = {"name":"vikas"}
student["name"]
'vikas'
student["age"]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    student["age"]
KeyError: 'age'
student["age"] =23
student
{'name': 'vikas', 'age': 23}
>>> student["age"] = 22
>>> student
{'name': 'vikas', 'age': 22}
>>> del student ["age"]
>>> student
{'name': 'vikas'}
>>> len(student)
1
>>> student.get
<built-in method get of dict object at 0x000002944EFC8DC0>
>>> student.pop ["age"]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    student.pop ["age"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> student.pop "age")
SyntaxError: unmatched ')'
>>> student.pop ("age")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    student.pop ("age")
KeyError: 'age'
>>> student.pop ('age')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    student.pop ('age')
KeyError: 'age'
>>> student.pop
<built-in method pop of dict object at 0x000002944EFC8DC0>
>>> student.keys()
dict_keys(['name'])
>>> students.items()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    students.items()
NameError: name 'students' is not defined. Did you mean: 'student'?
>>> student.items()
dict_items([('name', 'vikas')])
>>> sorted(student)
['name']
>>> min(student)
'name'
>>> max(student)
'name'
>>> student.copy()
{'name': 'vikas'}
