Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a =10
>>> b =10.3
>>> c = 'ramesh'
>>> print (a,b,c)
10 10.3 ramesh
>>> print ("a value is ",a)
a value is  10
>>> print (" a value is ",a ,| "b value is ",b,'| c value is ' c)
SyntaxError: invalid syntax
>>> print (" a value is ",a ,| b value is ",b,'| c value is',c)
...        
SyntaxError: unterminated string literal (detected at line 1)
>>> print ("a value is",a,"| b value is",b,'| c value is',c)
...        
a value is 10 | b value is 10.3 | c value is ramesh
>>> print (a,b,c)
...        
10 10.3 ramesh
>>> print( a,b,c sep=' ')
...        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print (f'a={a} b={b} c={c}')
...        
a=10 b=10.3 c=ramesh
>>> print ("f a value is {a} | b value is {b} | c value is {c}")
...        
f a value is {a} | b value is {b} | c value is {c}
>>> print('a%d b+%f c%s'%(a,b,c))
...        
a10 b+10.300000 cramesh
>>> print('a%d b%f c%s'%(a,b,c))
...        
a10 b10.300000 cramesh
>>> print('a=%d b=%f c=%s'%(a,b,c))
...        
a=10 b=10.300000 c=ramesh
>>> print( 'a={} | b={} | c={}')
...        
a={} | b={} | c={}
