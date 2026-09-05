'''def display(name,email,password):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')
    display('xyz','xyz@gmail.com','xyz@123')
    display('xyz@123','xyz@gmail.com','xyz')
    display('xyz@gmail','xyz@gmail.com','xyz')'''


'''
def display(name,email,password):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')
    display(name='xyz',email='xyz@gmail.com',password='xyz@123')
    display(password='xyz@123',email='xyz@gmail.com',name='xyz')
    display(email='xyz@gmail',password='xyz@gmail.com',name='xyz')'''



'''def display(name,email='gmail.com',password=''):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')
    display('xyz','xyz@gmail.com','xyz@123')
    display('xyz''xyz@gmail.com',)
    display('xyz')'''


'''
def display(*names):
    print(names)
    display('Avinash')
    display('vikas','Anil')
    display('mouli','Appu')
    display('narasimha','Ganesh','Phani')'''


def display(**products):
    print(products)
    display(bag=500)
    display(bag=5000,book=30)
    display(bag=500,book=30,bottle=90)