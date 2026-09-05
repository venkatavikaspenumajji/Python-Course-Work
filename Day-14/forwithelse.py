'''for i in range(1,10):
    if i==15:
        break
    print(i)
else:
    print("end of the loop")'''



'''pin = 2345
for _ in range(4):
    epin=int(input("enter the pin:"))
    if pin == epin:
        print("unlock")
    else:
        print("invalid")
else:
    print("after ")'''


'''n = int(input("enter the number:"))
print("factrors:", end='')
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')'''


n =  int(input("enter the number:"))
if n<=1:
    print("not  prime number")
else:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
        print("prime number")



