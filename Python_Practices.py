# Python Practices:
 a=[1,2,3]
b=a
c=b
print(a is c)
print(a==c)
import sys
import time
def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
        print()
def print_lyrics():
    lyrics = [
"We're only getting older, baby",
"And I've been thinking about it lately",
"Does it ever drive you crazy",
"Just how fast the night changes?",
"Everything that you've ever dreamed of",
"Disappearing when you wake up",
"But there's nothing to be afraid of",
"Even when the night changes",
"It will never change me and you",
]
    delays = [1.6, 1.4, 1.8, 2.1, 2.4, 1.7, 2.0,2.0,1.7]
    print("\n🎧 Now Playing: “ NIGHT CHANGES ” — ONE DIRECTION\n")
    time.sleep(1.5)
    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])
        print_lyrics()

a=[1]
b=[1]
print(a is b)
print(a==b)
a=[
    {'name':'ashok','salary':20},
    {'name':'ramya','salary':30},
    {'name':'aruna','salary':40}
]
print(a)
print(len(a))
print(sum(object['salary'] for object in a))
print(sum(object['salary'] for object in a) / len(a))    #---"""average_salary---"""
# a[0]['salary']=1
# print(a)
high_salary=max(object['salary'] for object in a)
print(high_salary)                                        #---"""high_salary---"""
min_salary=min(object['salary'] for object in a)
print(min_salary)                                        #---"""min_salary---"""



limit=20
a=0
b=1
count=0
for i in range(limit):
    if a>limit:
        break
    print(a,end=' ')
    a,b=b,a+b
    count+=1
print("\nTotal fibonacci numbers:",count)
a=[a,b,c]
b=[1,2,3]
a.append(b)
print(a)

a=[1,2,3]
b=[1,2,3]
a.extend(b)
print(a)

import time

currenttime= time.localtime(time.time())
print ("Current time is", currenttime) 
a=[1,2,3,4,5]
print([a[::-2]])
nums=(1,2,3,4,5)
for ash in nums:
    if ash==3:
        pass
    else:
        print("ramya")
for i in range(1,6):
    if i==3:
        continue
else:
    print("ashok")

for i in range(1,6):
    if i==3:
        break
    print(i)

for i in range(1,6):
    if i==3:
        pass
    print(i)
x=5
y=0
print(x//y)

    

import traceback
try:
    x=10
    y=0
    print(x//y)
except Exception as e:
    traceback.print_exc()
    print(e)
else:
    print("No exceptions occurred")
finally:
    print("Execution completed")


----with else block----:

try:
    x=10
    y=2
    print(x//y)
except Exception as e:
    traceback.print_exc()
    print(e)
else:
    print("No exceptions occurred")
finally:
    print("Execution completed")


class myexception(Exception):
    pass
def check_age(age):
    if age<0:
        raise myexception("Age cannot be negative")
    else:
        print(f"Your age is {age}")
        try:
            age=int(input("Enter your age: "))
            check_age(age)
        except myexception as me:
            print("Custom Exception:",me)

Map function:

l=["1","2","3","4","5"]
result=(list(map(int,l)))
print(result)
print(list(result))
print(type(result))

def double(i):
    return i * 2

asd=list(map(double,result))
print(asd)

Lamba function with map:
a=[1,2,3,4,5]
result=list(map(lambda x:x*2,a))
print(result)

b=[6,7,8,9,10]
result2=list(map(lambda x,y:x+y,a,b))
print(result2)

f=lambda x:"junior" if x<18 else "senior"
print(f(20))
# --------------------------------------------------------