for i in range(6):
    print(" " * (6-i) + "*" * (2*i-1))
for i in range(6-1,0,-1):
    print(" " * (6-i) + "*" * (2*i-1))



count=0
for i in range(1,6):
    for j in range(i):
        count=count+1
        print(count,end=" ")
    print()

# for i in range(1,6):
#     print(" " * (5-i),end="")
#     for j in range(5,i-1,-1):
#         print(j," ",end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(5,i,-1):
#         print(j,end=" ")
#     print()
# 5 
# 5 4
# 5 4 3
# 5 4 3 2

# for i in range(5,0,-1):
#     for j in range(i,5+1):
#         print(j,end=" ")
#     print()
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# # 1 2 3 4 5
# for i in range(5,0,-1):
#     for j in range(i,5+1):
#         print(i,end=" ")
#     print()
# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1
# for i in range(5,0,-1):
#     for j in range():
#         print(j,end=" ")
#     print()
# count=1
# for i in range(1,5):
#     for j in range(i):
#         print(count,end=" ")
#         count=count+2
#     print()
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
    
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()
# count=0
# for i in range(1,6):
#     for j in range(1,6+1):
#         count=count+1
#         print(count,end=" ")
#     print()






