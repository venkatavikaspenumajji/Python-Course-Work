# Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
# Enter "help" below or click "Help" above for more information.
# a = {1,2,3,4,5}
# b ={2,4,5,6,7,}
# print(a| b)
# {1, 2, 3, 4, 5, 6, 7}
# print(a&b)
# {2, 4, 5}
# print(a - b)
# {1, 3}
# print(a^b)
# {1, 3, 6, 7}
# a = {1,2}
# b = {1,2,3,4,5}
# print(a.issubset(b))
# True
# print(a.isdisjoint(b))
# False
# print(b.issuperset(a))
# True
# min(a)
# 1
# max(a)
# 2
# sum(a)
# 3
# b=a
# b
# {1, 2}
# sorted(a)
# [1, 2]
# b=a
# b
# {1, 2}
# c =a.copy()
# c.add(13)
# c.add(15)
# c
# {1, 2, 13, 15}
# a
# {1, 2}
# a.update({12,3,45,67)}
# SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
# a.update({12,3,45,67)}
# SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
# a.update({12,3,45,67})
# a
# {1, 2, 67, 3, 12, 45}
# a.remove(3)
# a
# {1, 2, 67, 12, 45}
# a.clear
# <built-in method clear of set object at 0x0000022B3A04A0A0>
# a.clear
# <built-in method clear of set object at 0x0000022B3A04A0A0>
# a.clear(a)
# Traceback (most recent call last):
#   File "<pyshell#33>", line 1, in <module>
#     a.clear(a)
# TypeError: set.clear() takes no arguments (1 given)
# a.clear()
# >>> a
# set()
# >>> a.pop()
# Traceback (most recent call last):
#   File "<pyshell#36>", line 1, in <module>
#     a.pop()
# KeyError: 'pop from an empty set'
# >>> a.remove(12)
# Traceback (most recent call last):
#   File "<pyshell#37>", line 1, in <module>
#     a.remove(12)
# KeyError: 12
# >>> all(a)
# True
# >>> any(a)
# False
# >>> #dictionary
# >>> 
# >>> #dictionary
# >>> a= {"name":  "anil" , "age" : 40}
# >>> a.keys()
# dict_keys(['name', 'age'])
# >>> a.values()
# dict_values(['anil', 40])
# >>> a.items()
# dict_items([('name', 'anil'), ('age', 40)])
# >>> a.update({"age":12})
# >>> a
# {'name': 'anil', 'age': 12}
# >>> a.pop("age")
# 12
# >>> a.clear()
# >>> a
# {}
# >>> a.copy()
# {}
# >>> a.get("name")
# >>> a
# {}
# >>> a.get()
# Traceback (most recent call last):
#   File "<pyshell#55>", line 1, in <module>
#     a.get()
# TypeError: get expected at least 1 argument, got 0
# >>> print(a.get("name"))
# None
