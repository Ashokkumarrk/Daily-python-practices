# def name(s:str)->dict:
#     freq={}
#     for char in s:
#         if char in freq:
#             freq[char] +=1
#         else:
#             freq[char] =1
#     return freq
# print(name("ashokkumar"))
    
# s = "aashokkumar"
# count=0
# freq = {}
# for char in s:
#     if char in freq:
#         freq[char] += 1
#         count=count+1
#     else:
#         freq[char] = 1
#         # count=count+1

# print(freq)
# print(count)

# vowels:

# text="banananai"
# vowels="aaeiouAEIOU"
# count=0
# for char in text:
#     for v in vowels:
#         if char == v:
#             count=count+1
#             print(char,end=" ")
#             break
# print(count)


# number_frequency:
# a=[10,20,30,10,5,6,5]
# freq={}
# count=0
# for n in a:
#     if n in freq:
#         freq[n]=freq[n]+1
        
#     else:
#         freq[n]=1
# print(freq)
# for key in freq:
#     print(key,":",freq[key])

# sorting:

# a=[10,20,5,67,8]
# is_sorted=True
# for i in range(len(a)-1):
#     if a[i] > a[i + 1]:
#         is_sorted=False
#         break
# if is_sorted :
#     print("list already sorted")
# else:
#     print("list not sorted")

# arr=[1,2,3,4,5,5,4,3,1]
# is_sorted=True
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j] > arr[j + 1]:
#             arr[j],arr[j + 1] = arr[j + 1],arr[j]
# print(arr)


# perfect_number:

# n=int(input())
# sum=0
# for i in range(1,n):
#     if (n % i ==0):
#         sum = sum + i
# if sum ==n:
#     print(n,"perfect number")
# else:
#     print(n," not perfect number")
    
    
# number pallindrome:

# num=int(input())
# rev=0
# while num > 0:
#     rev=rev*10 + num % 10
#     num=num//10
# if num == rev:
#     print("pallindrome")
# else:
#     print("pallindrome")

# s = input("Enter a string: ")

# is_palindrome = True

# for i in range(len(s)):
#     if s[i] != s[len(s) - 1 - i]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# find maximum repeated values:

# data =[1,2,3,4,5,5,6,6,6,7,8]
# freq={}
# for item in data:
#     freq[item]=freq.get(item,0) + 1
# max_count=max(freq.values())
# result=[key for key,val in freq.items() if val == max_count]
# print("most repeated value",result)
# print("max_count",max_count)

# l=[1,2,3,4,5]
# for i in range(len(l)):
#     l[i]+=1
#     print(l)

# fibonacci:
# a,b=0,1
# while a < 10:
#     print(a,end=" ")
#     a,b=b,a+b

# n=20
# a,b=0,1
# for _ in range(n):
#     print(a,end=" ")
#     a,b=b,a+b

# limit=100
# a,b=0,1
# while a < limit:
#     print(a,end=" ")
#     a,b=b,a+b

# armstrong & neon & prime & strong & perfect:

# num=int(input())
# total=0
# digits=len(str(num))
# temp=num
# while temp > 0:
#     rem=temp%10
#     total = total + rem ** digits
#     temp=temp//10
# if total == num:
#     print("pallindrome")
# else:
#     ("not a pallindrome")

# neon number:
# num=int(input())
# total=0
# square = num*num
# while square > 0:
#     rem=square % 10
#     total = total + rem
#     square=square//10
# if total == num:
#     print("neon ")
# else:
#     ("not a neon number")

# strong_number:
# num=int(input())
# total=0
# temp=num
# while temp > 0:
#     digit=temp%10
#     fact=1
#     for i in range(1,digit+1):
#         fact = fact * i
#     total = total + fact
#     temp=temp//10
# if total == num:
#     print("strong number")
# else:
#     print("not a strong number")

# Prime number:

# num = int(input())
# if num <=1:
#     print("not prime")
# else:
#     for i in range(2,num):
#         if num % i ==0:
#             print("not prime")
#             break
#     else:
#         print("prime number")
