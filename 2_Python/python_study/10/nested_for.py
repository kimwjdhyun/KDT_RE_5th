"""
for y in range(5): # y:0 -> 1-> 2-> 3-> 4
    for x in range(1, 11): # x: 1 ~ 10
        print(x, end= " ")
    print()
"""

for i in range(1, 11):
    for j in range(1, i+1):
        print("*", end="")
    print()
