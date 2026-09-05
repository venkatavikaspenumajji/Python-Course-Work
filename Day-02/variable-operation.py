Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
... A=10
... a
... 10
... A
... 10
... a=b=c=20
... a
... 20
... 20
... c
... 20
... a,b,c=30
... Traceback (most recent call last):
...   File "<pyshell#8>", line 1, in <module>
...     a,b,c=30
... TypeError: cannot unpack non-iterable int object
... a,b,c=10,20,30
... a
... 10
... b
... 20
... c
... 30
... a,b=b,a
... a
... 20
... b
... 10
... del c
... c
SyntaxError: multiple statements found while compiling a single statement
