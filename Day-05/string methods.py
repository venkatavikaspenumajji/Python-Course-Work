# Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
# Enter "help" below or click "Help" above for more information.
# c =' python programming'
# len(c)
# 19
# ord('p')
# 112
# ord('a')
# 97
# chr(65)
# 'A'
# chr(66)
# 'B'
# min(c)
# ' '
# max(c)
# 'y'
# sorted(c)
# [' ', ' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
# print(len(c))
# 19
# c ='python programming'
# c
# 'python programming'
# c.upper()
# 'PYTHON PROGRAMMING'
# c.lower
# <built-in method lower of str object at 0x000001E50519B430>
# c.lower()
# 'python programming'
# c.
# SyntaxError: invalid syntax
# c.capitalize()
# 'Python programming'
# c.swapcase()
# 'PYTHON PROGRAMMING'
# 'ashbdjfwonmdopjwdfbhj' .casefold()
# 'ashbdjfwonmdopjwdfbhj'
# c.center(50,'7')
# '7777777777777777python programming7777777777777777'
# c.rjust(46,'-')
# '----------------------------python programming'
# '12'.Zfill(4)
# Traceback (most recent call last):
#   File "<pyshell#21>", line 1, in <module>
#     '12'.Zfill(4)
# AttributeError: 'str' object has no attribute 'Zfill'. Did you mean: 'zfill'?
# `'12'.zfill(4)
# SyntaxError: invalid syntax
# '12'.zfill(4)
# '0012'
# c.find()
# Traceback (most recent call last):
#   File "<pyshell#24>", line 1, in <module>
#     c.find()
# TypeError: find expected at least 1 argument, got 0
# c.find('l')
# -1
# c.rfind('i')
# 15
# c
# 'python programming'
# c.index('d')
# Traceback (most recent call last):
#   File "<pyshell#28>", line 1, in <module>
#     c.index('d')
# ValueError: substring not found
# c. index('o')
# 4
# c.rindex('m')
# 14
# c.replace('string', 'Float')
# 'python programming'
# c.replace ('i','o')
# 'python programmong'
# c.marketrans('aeiou','12334')
# Traceback (most recent call last):
#   File "<pyshell#33>", line 1, in <module>
#     c.marketrans('aeiou','12334')
# AttributeError: 'str' object has no attribute 'marketrans'. Did you mean: 'maketrans'?
# >>> c.maketrans('aeiou','12334')
# {97: 49, 101: 50, 105: 51, 111: 51, 117: 52}
# >>> c.translate(c.maketrans('aeiou','12345'))
# 'pyth4n pr4gr1mm3ng'
# >>> c.split()
# ['python', 'programming']
# >>> p.splitlines()
# Traceback (most recent call last):
#   File "<pyshell#38>", line 1, in <module>
#     p.splitlines()
# NameError: name 'p' is not defined
# >>> c.splitlines()
# ['python programming']
# >>> " ".join(["hello", "vikas"])
# 'hello vikas'
# >>> "apple-pie".partition("-")
# ('apple', '-', 'pie')
# >>> "apple-pie".rpartition("-")
# ('apple', '-', 'pie')
# >>> "a,b,c".rsplit(",",1)
# ['a,b', 'c']
# >>> c.strip()
# 'python programming'
# >>> c.lstrip()
# 'python programming'
# >>> c.rstrip()
# 'python programming'
# >>> c.encode()
# b'python programming'
# >>> c.decode()
# Traceback (most recent call last):
#   File "<pyshell#48>", line 1, in <module>
#     c.decode()
# AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
# >>> 'hello'. decode("utf-8")
# Traceback (most recent call last):
#   File "<pyshell#49>", line 1, in <module>
#     'hello'. decode("utf-8")
# AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
# >>> b'hello'. decode("utf-8")
# 'hello'
