Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={23,34,12,27,56,}
set(a)
{34, 23, 56, 27, 12}
int(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'set'
list(a)
[34, 23, 56, 27, 12]
tuple(a)
(34, 23, 56, 27, 12)
>>> bool(a)
True
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dict(a)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> complex(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    complex(a)
TypeError: complex() argument must be a string or a number, not set
>>> a={1,2,3,4,5}
>>> str(a)
'{1, 2, 3, 4, 5}'
>>> float(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'set'
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
>>> tuple(a)
(1, 2, 3, 4, 5)
>>> set(a)
{1, 2, 3, 4, 5}
>>> list(a)
[1, 2, 3, 4, 5]
>>> bool(a)
True
>>> complex(a)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    complex(a)
TypeError: complex() argument must be a string or a number, not set
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(a)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
