Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> int(a)
10
>>> float(a)
10.0
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> complex(a)
(10+0j)
>>> boolean(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    boolean(a)
NameError: name 'boolean' is not defined
>>> bool(a)
True
>>> str(a)
'10'
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> a=10.1
>>> float(a)
10.1
>>> int(a)
10
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(a)
TypeError: 'float' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(a)
TypeError: 'float' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(a)
TypeError: 'float' object is not iterable
bool(a)
True
dict(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(a)
TypeError: 'float' object is not iterable
str(a)
'10.1'
complex(a)
(10.1+0j)
a=10+4k
SyntaxError: invalid decimal literal
a = 3+2j
complex(a)
(3+2j)
int(a)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
str(a)
'(3+2j)'
list(a)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list(a)
TypeError: 'complex' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    set(a)
TypeError: 'complex' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    tuple(a)
TypeError: 'complex' object is not iterable
dic(a)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    dic(a)
NameError: name 'dic' is not defined. Did you mean: 'dir'?
bool(a)
True
True
True
a={2,3,4,5,6}
set(a)
{2, 3, 4, 5, 6}
int(a)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(a)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'set'
list(a)
[2, 3, 4, 5, 6]
tuple(a)
(2, 3, 4, 5, 6)
bool(a)
True
dict(a)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dict(a)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
str(a)
'{2, 3, 4, 5, 6}'
a=(23,56,78,90,24)
tuple(a)
(23, 56, 78, 90, 24)
int(a)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(a)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'tuple'
list(a)
[23, 56, 78, 90, 24]
set(a)
{78, 23, 56, 24, 90}
dict(a)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dict(a)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
str(a)
'(23, 56, 78, 90, 24)'
complex(a)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    complex(a)
TypeError: complex() argument must be a string or a number, not tuple
bool(a)
True
