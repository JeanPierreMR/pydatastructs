from pydatastructs import SparseTable
from time import sleep
from random import randint

size = 10000

def random_array(size):
    size = int(size)
    array = []
    for x in range(size):
        array.append(randint(-9999, 9999))
    return array

def test_trie(size):
    #100
    array = random_array(size/10)
    st = SparseTable(array)
    sleep(1)
    #1 000
    array = random_array(size / 2)
    st = SparseTable(array)
    sleep(1)
    # 100 000
    array = random_array(size)
    st = SparseTable(array)
    sleep(1)
    for x in range(int(size/10)):
        A = randint(0, size-2)
        st.query(A, randint(A, size-1))


if __name__ == "__main__":
    test_trie(size)