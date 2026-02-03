# # for i in range(5):
# #     print("1",end=" ")
# # for i in range(1,6):
# #     print(i,end=" ")
# # for i in range(1,10,2):
# #     print(i,end=" ")
# # for i in range (100):
# #     if i % 3==0 and i%5==0:
# #         print(i,end=" ")  its for mutual 3 and 5
# # for i in range (100):
# #     if i % 3==0 or i%5==0:
# #         print(i,end=" ")    its for either 3 or 5
# # a=int(input())
# # for i in range(100):
# #     if i % a==0:
# #         print(i)         divisors for given number

# # count of divisors numbers:
# # a=int(input())
# # count=0
# # for i in range(100):
# #     if i % a==0:
# #         count=count+1
# # print(count)

# # prime number:

# # n = 27
# # count = 0

# # for i in range(1, n+1):
# #     if n % i == 0:
# #         count += 1

# # if count == 2:
# #     print("Prime Number")
# # else:
# #     print("Not Prime")

# # #reverse printing number:
# # n=12345
# # reverse = 0
# # while n > 0:
# #     digit = n % 10
# #     reverse = reverse * 10 + digit
# #     n = n // 10

# # print(reverse)

# # # count of digits:
# # n=12345678
# # count=0
# # while n > 0:
# #     n = n // 10
# #     count=count+1
# # print(count)

# # # sum of digits:
# # n=12345678
# # sum=0
# # while n > 0:
# #     digit = n % 10
# #     sum = sum + digit
# #     n = n // 10
# # print(sum)

# # # rev
# # num=1234
# # rev=0
# # while num>0:
# #     digit=num%10
# #     rev=rev*10+digit
# #     num=num//10
# # print(rev)

# # a="madam"
# # rev=0
# # if a==a[::-1]:
# #     print("palindrome")
# # print("not palindrome")
# # for i in range(6):
# #     print("()"* i)
# # for i in range(6):
# #     print("(" * i, ")" * i )
# # n=197
# # sum=0
# # for i in range(n):
# #     num=n%10
# #     num=num//10
# #     print(sum)
# # right angeled traingle:

# # n=9
# # for i in range(10):
# #     print("*"*i)  
# # for i in range(10,0,-1):
# #     print("*"*i)  

# #  pyramid:
 
# # num=int(input())
# # for i in range(1,num+1):
# #     spaces=num-i
# #     stars=2*i-1
# #     print(" " * spaces + "*" * stars)

# # n=8
# # # spaces=n-1
# # # stars=2*i-1
# # for i in range(1,n+1):
# #     spaces=n-i
# #     stars=2*i-1
# #     print(" " * spaces + "*" * stars)
# # for i in range(n-1,0,-1):
# #     print("" * spaces + "*" * stars)
# # n=5
# # for i in range(1,n+1):
# #     print(" " * (n-i) + "*" * (2*i-1))
# # print("hello")
# #  pyramid:

# # for i in range(8):
# #     print(" " * (8-i) + "*" * (2*i-1))
# # for j in range(8,0,-1):
# #     print(" " * (8-j) + "*" * (2*j-1))
# # #  spaces = n-i
# # # stars = 2*i-1

# # # square star pattern:
# # for i in range(5):
# #     for j in range(5):
# #         print("*",end="")
# #     print()

# # name="ashokkumar"
# # result=""
# # for i in range(len(name)):
# #     if i % 2==0:
# #         result += name[i].upper()
# #     else:
# #         result += name[i].lower()
# # print(result)

# # name="ashok1234"
# # print(name.upper())
# # print(ord('1'))       # ascii value


# # name='ashokkumar123'
# # result=" "
# # for char in name:
# #     if 'a' <= char <= 'z':
# #         result += chr(ord(char) - 32)
# #     else:
# #         result += char


# # print(result)

# # password validator without builtin functions:
# # password = input("Enter your password: ")
# # upper = False
# # lower = False
# # digit = False
# # special= False

# # for char in password:
# #     if 'A' <= char <= 'Z':
# #         upper = True
# #     elif 'a' <= char <= 'z':
# #         lower = True
# #     elif '0' <= char <= '9':
# #         digit = True
# #     else:
# #         special = True

# # if upper and lower and digit and special:
# #     print("Password is valid")
# # else:
# #     print("Password is invalid")
    

# # for i in range(8):
# #     print(" " * (8-i) + "*" * (2*i-1))
# # for i in range(8,0,-1):
# #     print(" " * (8-i) + "*" * (2*i-1))
# # spaces=n-i
# # stars=2*i-1

# # password generator without builtin functions:
# # import random
# # def generate_password(length=12):
# #     upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# #     lower_chars = "abcdefghijklmnopqrstuvwxyz"
# #     digits = "0123456789"
# #     special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

# #     all_chars = upper_chars + lower_chars + digits + special_chars
# #     password = ""

# #     for _ in range(length):
# #         index = random.randint(0, len(all_chars) - 1)
# #         password += all_chars[index]

#     return password
# import numpy as np
# array=np.random.randint(1,100,size=(3,4))
# print(array)
# email validator without builtin functions:
# email = input("Enter your email: ")
# at_count = 0
# dot_count = 0
# for char in email:
#     if char == '@':
#         at_count += 1
#     elif char == '.':
#         dot_count += 1
# if at_count == 1 and dot_count >= 1:
#     print("Valid email")
# else:
#     print("Invalid email")
