import math

def sparsetableConstruction(arr):
    length = len(arr)
    sparsetable = [[-1 for i in range(length)]
    for j in range(int(math.log(length,2))+1)
    ]
