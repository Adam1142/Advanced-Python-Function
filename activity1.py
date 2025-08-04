#Add 2 Lists using map and lambda:
L1 = [1, 2, 3]
L2 = [4, 5, 6]
result = map(lambda x, y : x + y, L1, L2)
print("Addition of 2 Lists")
print(list(result))

#Using map:
L3 = [1, 2, 3, 4, 5]
def sq (L):
    return L*L
var1 = list(map(sq, L3))
print("Square of the numbers in the list:")
print(var1)