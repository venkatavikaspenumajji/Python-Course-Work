'''def display(name, email,password):
    print(f' hellow{name},')
    print(f' your email:{email},')
    print(f' your password{password},')
    display('vikas','vikas@email.com','vikas@123')
    display('Avinash','Avinash@email.com','Avinash@123')
    display('Narashima','Narashima@email.com','Narashima@123')
    display('anil','anil@email.com','anil@123')'''

'''
def isleapyear(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} it is not a leap year")

for year in range(2001,2027):
    isleapyear(year)'''


'''
def sumofdigits(n):
    sum=0
    while n>0:
        sum +=n%10
        n=n//10
        return sum
    n= int(input("enter the number"))
    print(f'sum of {n} digits is {sumofdigits(n)}')'''



'''def productsofdigits(n):
    pro=1
    while n>0:
        pro +=n%10
        n=n//10
        return pro
    n= int(input("enter the number"))
    print(f'product of {n} digits is {productofdigits(n)}')'''

'''
def checkpassword(password):
    if len(password)>8:
        check = set()
        for i in password:
            if i.isupper():
                check.add('u')
            elif i.islower():
                check.add('l')
            elif i.digit():
                check.add('d')
            else:
                check.add('s')
                if len(check)==4:
                    return "strong password"
                return "weak password" '''









