import math

class SparseTable():
    def __init__(self, arr):
        '''
            Notes about sparse table:
            The idea is to precompute minimum of all subarrays of size 2j where j varies from 0 to Log n.
            '''

        length = len(arr)
        sparsetable = [[-1 for i in range(length)]
                       for j in range(int(math.log(length, 2)) + 1)]

        for j in range(int(math.log(length, 2)) + 1):
            for i in range(length):
                minimum = i
                # 2^n (2)
                if (i + (2 ** j) - 1 < length):
                    for x in range(i, i + (2 ** j - 1)):
                        if (array[x] < array[minimum]):
                            minimum = x

                    sparsetable[j][i] = minimum
        self._data = sparsetable

    def query(self, arr, range):
        lengtharr = len(arr)
        minimumel = []

        while lengtharr > 0:
            b = int(math.log(len(arr),2))
            minimumel.append(arr[self._data[b][range[0]]])
            lengtharr = lengtharr - (2**b)

        return min(minimumel)

