'''def display(n):
    n=n+10
    print('inside:',n)

n=10
display(n)
print('outside:',n)
def display():
    print('inside:',n)'''


def display():
    print('inside:',n)
    n=10
    display()
    print('outside:',n)
    def display():
        n=10
        print('inside:',n)
        display()


    def display():
        global n
        n=n+10
        print('Inside:',n)
        n=10
        display() 
        n=10
        print('inside:',n)
        display()

 def display():
        global n
        n=n+10
        print('Inside:',n)
        n=10
        display() 
        n=10
        print('inside:',n)
        display()



        '''def display():
            global n
        n=n+10
        print('Inside:',n)
        n=10
        display() 
        n=10
        print('inside:',n)
        display()'''

'''def display():
     global n
     n='pfs'
     print("updates course:",n)

     n='jfs'
     display()
     print("final course:",n)'''



def display():
     n='jfs'
     def update():
          nonlocal n
          n='pfs'
          print("update course:",n)
          update()
          print("final course:",n)
display()


'''l=[1,2,3,4,5]
max=20
sum=10
print(sum)'''



def display(n):
     n[5]=6
     print("inside:",n)
     n={1:2,3:4}
     display(n)
     print('outside:',n)