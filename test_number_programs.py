# n=int(input())
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# n=int(input())
# a,b=0,1
# for i in range(1,n+1):
#     print(a,end=" ")
#     a,b=b,a+b

# n=int(input())
# total=0
# temp=n
# digits=len(str(n))
# while temp >0:
#     rem=temp%10
#     total=total + rem**digits
#     temp=temp//10
# if total==n:
#     print("armstrong number")
# else:
#     print("not a armstrong number")

# n=int(input())
# square=n*n
# total=0
# while square >0:
#     rem=square%10
#     total=total+rem
#     square=square//10
# if n==total:
#     print("neon number")
# else:
#     print("not a neon number")

# n=int(input())
# total=0
# temp=n
# while temp >0:
#     rem=temp%10
    
#     fact=1
#     for i in range(1,rem+1):
#         fact=fact*i
#     total=total+fact
#     temp=temp//10
# if total==n:
#     print("strong number")
# else:
#     print("no")

# n=int(input())
# total=0
# for i in range(1,n):
#     if n % i ==0:
#         total=total + i
# if total == n:
#     print("perfect number")
# else:
#     print("not a perfect number")

# n=int(input())
# total=0
# # temp=n
# while n<=0:
#     print("not prime")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         print("prime number")

# n=int(input())
# # temp=n
# rev=0
# while n>0:
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
# print(rev)

# n=int(input())
# temp=n
# rev=0
# while temp>0:
#     rem=temp%10
#     rev=rev*10+rem
#     temp=temp//10
# if n == rev:
#     print("pallindrome")
# else:
#     print("not pallindrome")

# n=int(input())
# total=0
# while n>0:
#     rem=n%10
#     total=total + rem
#     n=n//10
# print("sum of digits",total)

# n=int(input())
# count=0
# while n >0:
#     rem=n%10
#     count=count+1
#     n=n//10
# print(count)

n=int(input())
product=1
while n>0:
    rem=n%10
    product=product * rem
    n=n//10
print(product)
