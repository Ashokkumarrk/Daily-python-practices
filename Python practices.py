a,b=0,1
while a < 10:
        print(a,end=" ")
        a,b=b,a+b

s='madam'
if s == s[::-1]:
        print("pallindrome")
else:
        print("not pallindrome")

        

s='122'
if s == s[::-1]:
        print("yes")
else:
        print("no")

for i in range(1,10+1):
        print('*'* i)
for i in range(50,0,-1):
        print("ashok" * i)
for i in range(1,6+1):
        print(' ' * (6-i) + "*" * (2*i-1))
for i in range(6-1,0,-1):
        print(' ' * (6-i) + "*" * (2*i-1))
for i in range(8):
        for j in range(8):
                print("*" ,end="")
        print()
        
for a in range(1,11):
        print(a,end=" ")
s=[10,20,30,40,50]
s[0]
print("first element is:",s[0])
print("last element is:",s[-1])

b=[1,2,3,4]
b.append(5)
print(b)
        
c=[1,2]
c.append(5)
print(c)

d=[1,3,4]
d.insert(1,2)
print(d)

e=[1,2,3,4]
e.remove(2)
print(e)

a=[5,9,7,1,89]
a.sort()
print(a)
a.sort(reverse = True)
print(a)

a=[1,2,3,4,5,6,7,8,9,]
len(a)
print(len(a))

v=['apple','banana','mango']
if 'apple' in v:
        print("apple is here")
else:
        print("not here")

a=[1,2]
b=[3,4]
a.extend(b)
print(a)


