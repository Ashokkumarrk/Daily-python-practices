# for i in range(20,6,-1):
#     print(i,end=" ")

# for j in range(5,0,-1):
#     count_down=j
# for i in range(20,6,-1):
#     for j in range(5,0,-1):
#         count_down=j
            
#         # count_down=count_down -1
#     if count_down == 0:
#         print("")
#     print(i,end=" ")
#     count_down=count_down -1



# row_size = 5
# count_down = row_size

# for i in range(20,5,-1):
#     print(i,end=" ")
#     count_down = count_down - 1
#     if(count_down == 0):
#         print("")
#         row_size = row_size - 1
#         count_down = row_size
state=20
for col in range(5,0,-1):
    for _ in range(col):
        print(state,end=" ")
        state-=1
        
    print()