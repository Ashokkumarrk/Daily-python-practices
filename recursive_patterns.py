# def pattern(n,cur=1):
#     if cur > n :
#         return
#     print(* range(1,cur + 1))
#     pattern(n,cur+1)
# pattern(5)

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# def pattern(n,cur=1):
#     if cur > n :
#         return
#     print("* " * cur)
#     pattern(n,cur+1)
# pattern(5)

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

#  recursive pyramid :
# def pyramid(n,cur=1):
#     if cur>n:
#         return
#     print(" " * (n-cur) + "*" * (2*cur-1))
#     pyramid(n,cur+1)
# pyramid(6)

# def pyramid_bottom (n):
#     if n == 0:
#         return
#     print(" " * (6-n) + "*" * (2*n-1))
#     pyramid_bottom(n-1)
# pyramid_bottom(6)

# # loop method
# for i in range(7):
#     print(" " * (7-i) + "*" * (2*i-1))
# for i in range(7-1,0,-1):
#     print(" " * (7-i) + "*" * (2*i-1))

# zig pattern recursive:

# def zig (n,cur=0,reverse=False):
#     if cur ==n:
#         reverse = True
#     if reverse and cur <0:
#         return
#     spaces_left=cur if not reverse else -cur + n-1
#     spaces_right=n-1-spaces_left
#     print(" " * spaces_left + "*" + " " * spaces_right + "*")
#     next_val=cur + 1 if not reverse else cur -1
#     zig (n,next_val,reverse)
# zig(8)

# square with hollow center:
# n=8
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# output:
# * * * * * * * * 
# *             * 
# *             *
# *             *
# *             *
# *             *
# *             *
# * * * * * * * *

# def box(n,row=1):
#     if row > n:
#         return
#     if  row ==1 or row ==n:
#         print("*" * n)
#     else:
#         print("*" + " " * (n-2) + "*")
#     box(n,row+1)
# box(8)

# for i in range(8):
#     for j in range(8):
#         print("*",end=" ")
#     print()


# def square(n,row=1):
#     if row>n:
#         return
#     print("* " * n)
#     square(n,row+1)
# square(8)

#  right angled:
# n=5
# for i in range(1,n+1):
#     print("*" * i)

# recursive:
# def right(n,cur=1):
#     if cur > n:
#         return
#     print("*" * cur)
#     right(n,cur+1)
# right(8)


# inverted right triangle:
# def right_inverted(n,cur=1):
#     if cur > n:
#         return
#     print("*" * (n - cur + 1))
#     right_inverted(n, cur+1)
# right_inverted(8)

# print()

# left triangle:
def left(n, cur=1):
    if cur > n:
        return
    print(" " * (n - cur) + "*" * cur)
    left(n, cur+1)
left(8)

print()

# inverted left triangle:
def left_inverted(n, cur=1):
    if cur > n:
        return
    print(" " * (cur - 1) + "*" * (n - cur + 1))
    left_inverted(n, cur+1)
left_inverted(8)
    
