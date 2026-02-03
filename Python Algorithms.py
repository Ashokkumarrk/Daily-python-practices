suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = [(r, s) for s in suits for r in ranks]
print(deck[:5])   # First 5 cards print
print(len(deck))  # 52 cards total
import random
random.shuffle(deck)
print(deck[:5])
print(len(deck))
card=random.choice(deck)
print(card)
prob=4/52
print(prob)

## step 2: MATRIX(list of lists):
matrix=[[1,2,3],
         [4,5,6],
        [7,8,9]
        ]
print(matrix[2][2])
#---successfully learned about matrix (list of lists).

n=5
sum=0
for i in range(1,n+1):
    sum+=i
    print(sum)
## --- for pseudocode logic use.
## hierarchy tree begineer level:
    
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# create nodes
root = Node(10)
root.left = Node(5)
root.right = Node(20)

print("Root:", root.value)        # 10
print("Left child:", root.left.value)  # 5
print("Right child:", root.right.value) # 20
