# n=int(input())
# if n % 3==0 and n%5==0:
#     print("alphabeta")
# elif n%5==0:
#     print("beta")
# elif n%3 ==0:
#     print("alpha")
# else:
#     print("gamma")
    
# factorial number:
# n=int(input())
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact) 

# fibonacci :
# n=int(input())
# a,b=0,1
# for i in range(1,n+1):
#     print(a)
#     a,b=b,a+b

# armstrong number:

# n=int(input())
# temp=n
# digits=len(str(n))
# total=0

# while temp>0:
#     rem=temp%10
#     total=total + rem ** digits
#     temp=temp//10
# if total== n:
#     print("armstrong number")
# else:
#     print("not a armstrong number")

# neon number:
# n=int(input())
# total=0
# square=n*n

# while square>0:
#     rem=square%10
#     total=total + rem
#     square = square//10
# if total == n:
#     print("neon number")
# else:
#     print("not a neon number")

# strong number:

# n=int(input())
# temp=n
# total=0

# while temp>0:
#     rem=temp%10
    
#     fact=1
#     for i in range(1,rem+1):
#         fact=fact*i
#     total=total + fact
#     temp=temp//10
    
# if total == n:
#     print("strong number")
# else:
#     print("not a strong number")

# perfect number:

# n=int(input())
# total=0
# for i in range(1,n):
#     if n % i ==0:
#         total=total + i
# if total == n:
#     print("perfect number")
# else:
#     print("not a perfect number")
        
# #  prime number:

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

# reverse a number:

# n=int(input())
# rev=0
# while n>0:
#     rem=n%10
#     rev=rev * 10 + rem
#     n=n//10
# print(rev)

# pallindrome:

# n=int(input())
# temp=n
# rev=0
# while temp > 0:
#     rem=temp%10
#     rev=rev*10 + rem
#     temp=temp//10
# if rev == n:
#     print("pallindrome")
# else:
#     print("not a pallindrome")
    
# string pallindrome:

# s=input()
# rev=""
# for char in s:
#     rev=char + rev
# if rev == s:
#     print("pallindrome")
# else:
#     print(" not a pallindrome")

# sum of digits:

# n=int(input())
# total =0
# while n > 0:
#     rem=n%10
#     total=total+rem
#     n=n//10
# print("sum of digits:",total)

# count of digits:

# n=int(input())
# count=0
# while n>0:
#     count=count+1
#     n=n//10
# print("total digits",count)

# product of numbers:
# n=int(input())
# product=1
# while n>0:
#     rem=n%10
#     product=product*rem
#     n=n//10
# print(product)

# harshad number ( niven number):
# divisible by the sum of its own digits:

# n=int(input())
# total=0
# temp=n
# while temp > 0:
#     rem=temp%10
#     total = total + rem
#     temp=temp//10
# if n % total ==0:
#     print("harshad number")
# else:
#     print("its not a harshad number")

# automorphic number:
# square ends with the number itself:

# n=int(input())
# square=n*n
# if str(square).endswith(str(n)):
#     print("automorphic number")
# else:
#     print("not a automorphic number")

# without builtin:
# n=int(input())
# sq=n*n
# temp=n
# total=0
# while temp>0:
#     total=total + 1
#     temp=temp//10
# if sq % (10 ** total)==n:
#     print("automorphic number")
# else:
#     print("nott an automorphic numberz")
    
# spy number:
# sum of digits is equal to product of digits:
# n=int(input())
# temp=n
# total=0
# product=1
# while temp > 0:
#     rem=temp%10
#     total=total+rem
#     product=product * rem
#     temp=temp//10
# if product == total:
#     print("spy number")
# else:
#     print("not a spy number")

# duck number:
# n=int(input())
# temp=n
# is_zero=False
# while temp>0:
#     rem=temp%10
#     if rem == 0:
#         is_zero=True
#         break
#     temp=temp//10
# if is_zero:
#     print("duck number")
# else:
#     print("not a duck number")
    
# n = 5
# count = 1

# for _ in range(n):
#     for j in range(count):
#         print("*", end="")
#     print()
#     count += 2
    
# n=5
# count=0
# for i in range(1,n):
#     for j in range(count):
#         # count=count+2
#         print("*",end="")
#         # count=count+2
#     print()
#     count=count+5
    
    
    
