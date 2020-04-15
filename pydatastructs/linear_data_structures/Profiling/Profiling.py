from pydatastructs.linear_data_structures import (
    OneDimensionalArray, DynamicOneDimensionalArray, MultiDimensionalArray)
from pydatastructs.utils.raises_util import raises
from random import randint
import cProfile

def test_MultiDimensionalArray():
    MDA = MultiDimensionalArray
    i = 200 #iteraciones __setitem__
    j = 5 #iteraciones generales
    size = 20 #tamaño de las dimensiones
    while j >= 0:
        A = MDA(int, size, size, size, size)
        A.fill(randint(-20000, 20000))
        while i >= 0:
            A[randint(0,19)][randint(0,19)][randint(0,19)][randint(0,19)] = randint(-20000, 20000)
            i -= 1
        j -= 1

def main():
    print(cProfile.run("test_MultiDimensionalArray()"))

if __name__ == "__main__":
    main()