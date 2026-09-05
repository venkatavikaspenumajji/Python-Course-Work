Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a%b
0
a/b
2.0
a//b
2
a**b
10240000000000
a==b
False
a<b
False
a>b
True
a!=b
True
a>=b
True
a<=b
False
a+=b
c
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c
NameError: name 'c' is not defined
a+=5
a
35
a-=5
a
30
a*=45
a
1350
a//=12
a
112
a**=12
a
3895975992546975973113856
a%=13
a
1
a/=11
a
0.09090909090909091
n=20
n%2==0
True
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
n%2==0 not n%3==0
SyntaxError: invalid syntax
n
20
n<5
False
not n<5
True
# str list tuple set dict
s='ramesh'
'e' in s
True
'd' in s
False
'f' not in s
True
l=[1,2,3,4,6,]
'6' in l
False
6 in l
True
10 in l
False
3 not in l
False
t=(2,3,4,5,7,8)
2 in t
True
56 not in l
True
s={4,5,6,9,0,}
9 in s
True
8 not in s
True
dict { 'name':'vikas' ,'age':'23', 'branch':'it'}
SyntaxError: invalid syntax
d={ 'name':'vikas' ,'age':'23', 'branch':'it'}
age in d
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    age in d
NameError: name 'age' is not defined
>>> 'name' in d
True
>>> '23' not in d
True
>>> l=[1,2,3,4,5]
>>> id(l)
2664530155520
>>> m=[2,3,5,6,7]
>>> id(m)
2664485735360
>>> l is m
False
>>> n=l
>>> id(n)
2664530155520
>>> lis n
SyntaxError: invalid syntax
>>> l is n
True
>>> id(a)
2664529069296
>>> s={2,3,4,5,6}
>>> id(s)
2664529682368
>>> s.add(5)
>>> s
{2, 3, 4, 5, 6}
>>> #bitwise oprator
>>> 9 & 10
8
>>> 9/10
0.9
>>> 9|10
11
>>> 9^10
3
>>> 8>>7
0
>>> 9<<4
144
>>> 3~5
SyntaxError: invalid syntax
>>> ~34
-35
>>> ~37
-38
