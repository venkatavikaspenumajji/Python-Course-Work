'''s = 'python program'
for i in range (len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i,s[i])'''

'''
l = [23,45,56,78,90,33,44]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
         sum=sum+i
         print(i,l[i])
         print(sum)
'''

'''
num = int (input("enter a number:"))
fact = 1
for i  in range (1, num + 1):
    fact = fact *i
    print("factorial=", fact)'''

'''data={}
n = int(input("enter the number of students:"))
max_marks = 0
for i in range(n):
    name = input("enter the name:")
    marks = int(input("enter the marks:"))
    if marks > max_marks:
        max_marks = marks
        data[name] = marks
        print(data)
        print("maximum marks:",max_marks)
'''
n=input("enter the number of products:")
total_bill=0
for i in range(n):
    product = int(input("enter the product name:"))
    price = int(input("enter number of price:"))
    quality = int(input("enter the qulity:" ))
    final_price= price * quality
    total += final_price
    print("total bill", total_bill)







