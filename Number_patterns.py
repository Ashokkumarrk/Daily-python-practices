# first we go with number patterns :
# rows and columns are very impoertant for this core logics:

# n=5
# for rows in range(1,n+1):
#     for cols in range(1,n+1):
#         print(cols,end=" ")
#     print()
# output:   1 2 3 4 5
        #   1 2 3 4 5
        #   1 2 3 4 5
        #   1 2 3 4 5
        #   1 2 3 4 5

# n=5
# for rows in range(1,n+1):
#     for cols in range(1,n+1):
#         print(rows,end=" ")
#     print()
#  output :   1 1 1 1 1
            # 2 2 2 2 2
            # 3 3 3 3 3
            # 4 4 4 4 4
            # 5 5 5 5 5

# n=5
# for rows in range(1,n+1):
#     for cols in range(rows):
#         print(rows,end=" ")
#     print()
    
# output:
# 1 
# 2 2 
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# n=5
# for rows in range(1,n+1):
#     for cols in range(rows):
#         print(cols,end=" ")
#     print()

# output:
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

# n=5
# for rows in range(1,n+1):
#     for cols in range(1,rows):
#         print(cols,end=" ")
#     print()

# output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# n=5
# for rows in range(1,n+1):
#     for cols in range(1,n-1):
#         print(rows,end=" ")
#     print()
#  output: 
# 1 1 1 
# 2 2 2 
# 3 3 3
# 4 4 4
# 5 5 5

# n=5
# for rows in range(1,n+1):
#     for cols in range(1,n-1):
#         print(cols,end=" ")
#     print()
    
# ouput:
# 1 2 3 
# 1 2 3 
# 1 2 3
# 1 2 3
# 1 2 3

# n=5
# for rows in range(1,n-1):
#     for cols in range(1,n-1):
#         print(cols,end=" ")
#     print()
    
# output:
# 1 2 3 
# 1 2 3 
# 1 2 3

# n=5
# for rows in range(1,n-1):
#     for cols in range(1,n-1):
#         print(rows,end=" ")
#     print()
# output:
# 1 1 1 
# 2 2 2 
# 3 3 3

# n=5
# for rows in range(1,n-1):
#     for cols in range(1,n+1):
#         print(cols,end=" ")
    # print()
# output:
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5

# n=5
# for rows in range(1,n-1):
#     for cols in range(1,n+1):
#         print(rows,end=" ")
#     print()
# output:
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3

# n=5
# for rows in range(n,0,-1):
#     for cols in range(1,rows+1):
#         print(cols,end=" ")
#     print()
# output:
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3
# 1 2
# 1


# n=5
# for rows in range(1,n+1):
#     for cols in range(1,rows+1):
#         print(cols,end=" ")
#     print()

# output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# n=5
# for rows in range(5,0,-1):
#     for cols in range(1,rows+1):
#         print(rows,end=" ")
#     print()
# output:
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3
# 2 2
# 1

# n=5
# for rows in range(5,0,-1):
#     for cols in range(1,rows+1):
#         print(cols,end=" ")
#     print()
# output:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# n=5
# for a in range(5,0,-1):
#     print(a,end=" ")
# for b in range(5,1,-1):
#     print(b,end=" ")
# for c in range(5,2,-1):
#     print(c,end=" ")
# for d in range(5,3,-1):
#     print(d,end=" ")
# for e in range(5,4,-1):
#     print(e,end=" ")

# n = 5
# for i in range(n):
#     for j in range(n, i, -1):
#         print(j, end=" ")
#     print()
# output:
# 5 4 3 2 1 
# 5 4 3 2 
# 5 4 3 
# 5 4 
# 5 
 

# count=0
# for rows in range(6):
#     for cols in range(1,rows):
#         count=count+1
#         print(count,end=" ")
#     print()
#  output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# n=20
# count=6
# for i in range(count,0,-1):
#     for j in range(i):
#         print(n,end=" ")
#         n=n-1
#     print()
# output:
# 20 19 18 17 16 15 
# 14 13 12 11 10 
# 9 8 7 6
# 5 4 3
# 2 1
# 0

# for i in range(20,15,-1):
#     print(i,end=" ")
# for j in range(15,11,-1):
#     print(j,end=" ")
# for k in range(11,8,-1):
#     print(k,end=" ")
# for s in range(8,6,-1):
#     print(s,end=" ")
# for u in range(6,5,-1):
#     print(u,end=" ")

# n=5
# count=0
# for i in  range(n):
#     for j in range(n,i,-1):
#         count+=1
#         print(count,end=" ")
#     print()
# output:
# 1 2 3 4 5 
# 6 7 8 9 
# 10 11 12 
# 13 14 
# 15 
# n=8
# count=0
# for i in  range(n):
#     for j in range(1,i):
#         count+=1
#         print(count,end=" ")
#     print()
#  output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
#                          its will upgrade your logics.Dont memorize understand the logic.   