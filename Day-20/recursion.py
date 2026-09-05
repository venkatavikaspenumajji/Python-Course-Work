'''def hello(n):
    if n==0:#base case
        return
    print("hello")
    hello(n-1)# recursive call

hello(5)'''


'''def student(n):
    if n==1:
        return
    print("class")
    student(n-2)


student(3) '''



'''def displaysum(n):
    if n==0:
        return
    print("sum")
    displaysum(n-1)

displaysum(10)'''



'''def product(n):
    if n==1:# base case
        return 1
    return n *product(n-1) # recursive call
print(product(13))'''



'''def maximum(arr,n):
    if n==1: #base case
        return arr[0]
    return max(arr[n-1],maximum(arr,n-1))
numbers=[10,25,40,45,72]
print(maximum(numbers,len(numbers)))'''


'''s= 'python'
def print_word(word,n):
    if n==6:#base case
        return#base case
    print(word[:n+1])
    print_word(word,n+1)# recursive call


print_word("python",0)'''


'''prices = [3456,567,867,5678,2345]
res=list(map(lambda price:price - price*0.3,prices))
print(res)'''


'''names = {'vikas','Avinash','Anil','Appu','Lokesh'}
res=list(filter(lambda name:len(name)>5,names))
print(res)'''

'''from  functools import reduce
l= [3,567,6,24,123,435,462]
res= reduce(lambda sum , i:sum+i,l)
print(res)'''


