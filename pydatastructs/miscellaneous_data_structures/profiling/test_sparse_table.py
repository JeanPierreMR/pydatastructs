import pytest
from pydatastructs import SparseTable
from random import randint

sizes = [10, 10000]
n_iterations = 10
n_rounds = 10

def random_array(size):
    array = []
    for x in range(size):
        array.append(randint(-9999, 9999))
    return array

#functions
def overhead_creation(size):
    random_array(size)

def st_creation(size):
    array = random_array(size)
    st = SparseTable(array)

def st_query(st: SparseTable, size):
    left = randint(0, size - 2)
    right = randint(left, size - 1)
    st.query(left, right)

def simple_query(array, size):
    left = randint(0, size - 2)
    right = randint(left, size - 1)
    min = array[0]
    for x in range(left, right+1):
        if array[x] < min:
            min = array[x]


size = sizes[0]
@pytest.mark.benchmark(group="Table size " + str(size))
def test_st_overhead_creation(benchmark):
    keyword_args = {'size': size}
    benchmark.pedantic(overhead_creation, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Table size " + str(size))
def test_st_creation(benchmark):
    keyword_args = {'size': size}
    benchmark.pedantic(st_creation, kwargs=keyword_args, iterations=1, rounds=n_rounds)

@pytest.mark.benchmark(group="Table size " + str(size))
def test_st_query(benchmark):
    array = random_array(size)
    st = SparseTable(array)
    keyword_args = {'size': size, 'st': st}
    benchmark.pedantic(st_query, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Table size " + str(size))
def test_query(benchmark):
    array = random_array(size)
    keyword_args = {'size': size, 'array': array}
    benchmark.pedantic(simple_query, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)

size = sizes[1]
@pytest.mark.benchmark(group="Table size " + str(size))
def test_st_overhead_creation2(benchmark):
    keyword_args = {'size': size}
    benchmark.pedantic(overhead_creation, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Table size " + str(size))
def test_st_creation2(benchmark):
    keyword_args = {'size': size}
    benchmark.pedantic(st_creation, kwargs=keyword_args, iterations=1, rounds=n_rounds)

@pytest.mark.benchmark(group="Table size " + str(size))
def test_st_query2(benchmark):
    array = random_array(size)
    st = SparseTable(array)
    keyword_args = {'size': size, 'st': st}
    benchmark.pedantic(st_query, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Table size " + str(size))
def test_query2(benchmark):
    array = random_array(size)
    keyword_args = {'size': size, 'array': array}
    benchmark.pedantic(simple_query, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)