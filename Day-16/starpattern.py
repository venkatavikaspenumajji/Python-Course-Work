'''rows = int(input("enter the number of rows:"))
for i in range(1, rows +1):
    for j in range(i):
        print("*",end=" ")
    print()'''


'''
n= int(input("enter the size:"))
for i in range(n):
    for sp in range(n-i-1):
        print('',end=" ")
        for j in range(i+1):
            print('*',end=" ")
        print()'''
'''
n = int(input("enter the size:"))
for i in range(n):
    for sp in range (i):
        print(' ',end=" ")
        for j in range( n-i):
            print('*',end=" ")
        print()'''

'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print('*',end='')
        else:
            print('',end='')
        print()'''

'''
n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1 or i==n//2 or j==n//2):
            print('*',end='')
        else:
            print('',end='')
        print()'''


'''
n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if (i==j or i+j = n-1):
            print('*',end='')
        else:
            print('',end='')
        print()'''

'''
n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if (i == 0 or j == 0 or i == n-1 or j == n-1):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''

n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (i == 0 or j == 0 or i == n-1 or j <=m):
            (j==m and i>=m) or (i==m and j>=m)
            (j==n-1 and i>=m)
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

''''
n = int(input('Enter the size: '))
for i in range(1, n+1):
    print('* ' + "  " * (n-i) + "*")
for i in range(1, n):
    print("* " + "  " * (i) + "*")'''











