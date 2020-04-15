import math

def sparsetableConstruction(arr):
    '''
    Notes about sparse table:
    The idea is to precompute minimum of all subarrays of size 2j where j varies from 0 to Log n.
    '''
    length = len(arr)
    sparsetable = [[-1 for i in range(length)]
    for j in range(int(math.log(length,2))+1)
    ]

    for j in range(int(math.log(length, 2))+1):
        for i in range(length):
            minimum = i
            if (i+(2**j)-1 < length):
                for a in range(i, i+(2**j-1)):
                    if (array[x] < array[minimum]): 
                        minimum = a
                
                sparsetable[j][i] = minimum 
    
    return sparsetable



def query():
