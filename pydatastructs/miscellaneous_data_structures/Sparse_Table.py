'''
API

Query:
The class Query's purpose is to represent a query range.

Attributes:
a and b - ranges minimum for comparison 

Methods:

sparsetableconstruction(list,int): fills table 
query(list, int, int):
rmq(list, int, list, int):
'''
'''
        Represents a trie data structure.

        Parameters
        ==========
        dtype: type
            A valid object type.
        N: number of keys in trie
        K: world inserting or searching 
        alphabet_size: size of alphabet *26

        Raises
        ======
        IndexError: 
            list index out of range
        TypeError: 
            object of type 'int' has no len()

        Examples
        ========
        >>> from pydatastructs import trie_structure as 
        >>> key = ["hi","bye"]
        >>> output = ["Not present in trie", 
              "Present in trie"] 
        >>> new = Trie()
        >>> for key in keys: 
               new.insert(key)
        >>> output[new.search("bye")]
        "Present in trie"
        >>> output[new.search("the")]
        "Not present in trie"

        References
        ==========
        .. [1] https://www.geeksforgeeks.org/range-minimum-query-for-static-array/
        .. [2] https://www.youtube.com/watch?v=c5O7E_PDO4U
        '''
import math 
from math import log2 

'''
Notes about sparse table
The idea is to precompute minimum of all subarrays of size 2j where j varies from 0 to Log n.
Importing log2 utilized for constructing a sparse table
Sparse table: precompute minimum of all subarrays of size 2j where j varies from 0 to Log n.
Parts of sparse table: construction, query and range minimum query
'''

Max = 500

table = [[0 for i in range(500)] 
			for j in range(500)] 


class Query: 
	def __init__(self, a, b): 
		self.A = a
		self.B = b

def sparsetableconstruction(arr: list, n: int): 
	global table

	for i in range(n): 
		table[i][0] = i 

	j = 1 #little to bigger intervals
	while (1 << j) <= n: 

		# Compute minimum value for all intervals with size 2^j 
		i = 0
		while i + (1 << j) - 1 < n: 

			#comparition
			if (arr[table[i][j - 1]] < 
				arr[table[i + (1 << (j - 1))][j - 1]]): 
				table[i][j] = table[i][j - 1] 
			else: 
				table[i][j] = table[i +
							(1 << (j - 1))][j - 1] 

			i += 1  #adding 1 for each
		j += 1

def query(arr: list, A: int, B: int) -> int: 
	global table

	j = int(log2(B - A + 1)) #example:floor(Log2(10-2+1)) = 3

	#comparition again
	if (arr[table[A][j]] <=
		arr[table[B - (1 << j) + 1][j]]): 
		return arr[table[A][j]] 
	else: 
		return arr[table[B - (1 << j) + 1][j]] 
 
def rmq(arr: list, x: int, q: list, y: int): 

	sparsetableconstruction(arr, x) 

	#sum queries
	for i in range(y): 
 
		A = q[i].A
		B = q[i].B
 
		print("The minimum of [%d, %d] is %d" %(A, B, query(arr, A, B))) 


if __name__ == "__main__": 
	a = [4, 6, 1, 5, 7, 3] 
	x = len(a) 
	q = [Query(0, 2), Query(2, 4), Query(3, 5)] 
	y = len(q) 

	rmq(a, x, q, y) 








    #fuente: https://www.geeksforgeeks.org/range-minimum-query-for-static-array/