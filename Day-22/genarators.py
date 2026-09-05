'''def retrivedata():
    data = ['1..100','101..200','201..300','301..400','401..500']
    for i in data:
        yield i
    reels = retrivedata()
    while True:
            status = input("[s]croll or [q]uit:")
            if status == 's':
                print(next(reels))
            else:
                break'''



'''def even():
    i=0
    while True:
        i+=2
        yield i

n=50
res =even()
for i in range(n):
    print(next(res))'''







'''def factor(n):
    for i in range(1,n+1):
        if n % i ==0:

         yield i

n=50
res =factor(n)
for i in res:
  print(i)'''


'''n=3
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
        if count==2:
         print("it is prime number")
    else:
        print("not a prime number")'''


def numbers():
    i=1
    while i<=10:
        yield 1
        i+=1
        res=numbers()
        print(next(res))
        print(next(res))
        print(next(res))
        print(next(res))
        print(next(res))
        print(next(res))
        print(next(res))
        print(next(res))
        print(next(res))
        
    





    
