from math import log2

__all__ = [
    'SparseTable'
]

"""
API

Query:
The class Query's purpose is to represent a query range.


Attributes:
l and r - ranges minimum for comparison 
array - array to precompute
Methods:

query(int, int): returns minimum of array[] from point l to r.
rmq(list): returns a list of queries
    list -  {'L': int, 'R': int}
"""
'''
Issue #25
Notes about sparse table
The idea is to precompute minimum of all subarrays of size 2j where j varies from 0 to Log n.
Importing log2 utilized for constructing a sparse table
Sparse table: precompute minimum of all subarrays of size 2j where j varies from 0 to Log n.
Parts of sparse table: construction, query and range minimum query
'''


class SparseTable():
    """
    Represents a sparse table structure.

    Parameters
    ==========
    array: list of int

    Raises
    ======
    NameError:
        name 'b' is not defined
    TypeError:
        object of type 'char' has no len()

    Examples
    ========
    >>> from pydatastructs import sparse_table
    >>> a = [0, 1, 2, 3, 4, 5]
    >>> q = [{'L': 0, 'R': 1}, {'L': 1, 'R': 3}, {'L': 3, 'R': 5}]
    >>> st = SparseTable(a)
    >>> st.rmq(q)
    [0, 1, 3]

    References
    ==========
    .. [1] https://www.geeksforgeeks.org/range-minimum-query-for-static-array/
    .. [2] https://www.youtube.com/watch?v=c5O7E_PDO4U
    """

    def __init__(self, array: list):
        n = len(array)
        if n < 500:
            self.table = [[0 for i in range(500)]
                                  for j in range(500)]
        else:
            self.table = [[0 for i in range(n)]
                                  for j in range(n)]
        self.array = array


        for i in range(n):
            self.table[i][0] = i

        j = 1  # little to bigger intervals
        while (1 << j) <= n:
            # Compute minimum value for all intervals with size 2^j
            i = 0
            while i + (1 << j) - 1 < n:

                # comparition
                if (array[self.table[i][j - 1]] <
                        array[self.table[i + (1 << (j - 1))][j - 1]]):
                    self.table[i][j] = self.table[i][j - 1]
                else:
                    self.table[i][j] = self.table[i +
                                        (1 << (j - 1))][j - 1]

                i += 1  # adding 1 for each
            j += 1

    def rmq(self, queries: list):
        results = []

        for query in queries:
            left = query['L']
            right = query['R']
            results.append(self.query(left, right))
        return results

    def query(self, L: int, R: int) -> int:
        self.table
        j = int(log2(R - L + 1))  # example:floor(Log2(10-2+1)) = 3

        # comparition again
        if (self.array[self.table[L][j]] <=
                self.array[self.table[R - (1 << j) + 1][j]]):
            return self.array[self.table[L][j]]
        else:
            return self.array[self.table[R - (1 << j) + 1][j]]


