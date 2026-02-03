# for i in range(5):
#     print("1",end=" ")
# for i in range(1,6):
#     print(i,end=" ")
# for i in range(1,10,2):
#     print(i,end=" ")
# for i in range (100):
#     if i % 3==0 and i%5==0:
#         print(i,end=" ")  its for mutual 3 and 5
# for i in range (100):
#     if i % 3==0 or i%5==0:
#         print(i,end=" ")    its for either 3 or 5
# a=int(input())
# for i in range(100):
#     if i % a==0:
#         print(i)         divisors for given number

# count of divisors numbers:
# a=int(input())
# count=0
# for i in range(100):
#     if i % a==0:
#         count=count+1
# print(count)

# prime number:

# n = 27
# count = 0

# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1

# if count == 2:
#     print("Prime Number")
# else:
#     print("Not Prime")

# #reverse printing number:
# n=12345
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10

# print(reverse)

# # count of digits:
# n=12345678
# count=0
# while n > 0:
#     n = n // 10
#     count=count+1
# print(count)

# # sum of digits:
# n=12345678
# sum=0
# while n > 0:
#     digit = n % 10
#     sum = sum + digit
#     n = n // 10
# print(sum)

# # rev
# num=1234
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print(rev)

# a="madam"
# rev=0
# if a==a[::-1]:
#     print("palindrome")
# print("not palindrome")

    