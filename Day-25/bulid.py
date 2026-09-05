import sys
#print(sys.path)
#print(sys.version)
print("start")
sys.exit()
print("end")


print(math.pi)
print(math.e)

print(math.sqrt(36))
print(math.pow(2,3))

print(math.ceil(12.00001))
print(math.ceil(12.3))
print(math.ceil(12.6))
print(math.ceil(12.9999999))

print(math.floor(12.00001))
print(math.floor(12.3))
print(math.floor(12.3))


print(math.fabs(-10))
print(math.factorial(5))
print(math.gcd(8,24))
print(math.sin(30))
print(math.cos(0))
print(math.cosec(30))
print(math.degrees(30))
print(math.radians(30))



'''import random
#random.seed(10)
print(random.randint(1,10))
print(random.randint(100000,9999999))
print(random.random())
print(random.uniform(1,16))

l= ['R','P','S']
print(random.choice(l))
print(random.choices(l,k=2))

random.shuffle(l)
print(l)'''


from collections import Counter

s = 'python programming'
m = 'this is that is this is is '.split()
l = [1,1,1,1,3,3,3,2,2,4,4,4,23,12,45,67,88]
print(counter(s))
print(counter(l))
print(counter(m))


s = 'python programming'
m = 'this is that is this is is '.split()
l = [1,1,1,1,3,3,3,2,2,4,4,4,23,12,45,67,88]

d= defaultdict(int)
for i in s:
    d[i]+=1
    print(d)


