Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s =''
s
''
s = 'ramesh'
s
'ramesh'
'ramesh' + 'ramu'
'rameshramu'
'ramesh*ramu'
'ramesh*ramu'
'ramesh'*ramu
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    'ramesh'*ramu
NameError: name 'ramu' is not defined
>>> 'ramesh'*46'
SyntaxError: unterminated string literal (detected at line 1)
>>> 'ramesh'*46
'rameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshrameshramesh'
>>> s ='codegnan'
>>> s[5]
'n'
>>> s[-1]
'n'
>>> s[-2]
'a'
>>> names = 'vikas sai ramesh mouli'
>>> names[0]
'v'
>>> names[::-1]
'iluom hsemar ias sakiv'
>>> names[1:4]
'ika'
>>> names[0]
'v'
>>> #slicing
>>> names[0:5]
'vikas'
>>> names[:6}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> names[:5]
'vikas'
>>> names[5;2]
SyntaxError: invalid syntax
>>> names[5:2]
''
>>> names[::2]
'vkssirms ol'
>>> ramesh in names
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    ramesh in names
NameError: name 'ramesh' is not defined. Did you mean: 'names'?
>>> 'ramesh' in names
True
>>> 'ramu' not in names
True
