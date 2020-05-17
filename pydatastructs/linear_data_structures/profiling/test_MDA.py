import pytest
from pydatastructs import MultiDimensionalArray
from pydatastructs import Trie
from random import randint
from random_words import RandomWords

trie = Trie()
rw = RandomWords()
sizes = [10, 500]
n_iterations = 100
n_rounds = 50


def MDA_2D_set(array, size):
    array[randint(0, size-1), randint(0, size-1)] = randint(0, 9999)


def MDA_2D_get(array, size):
    array[randint(0, size-1), randint(0, size-1)]


def MDA_fill(array):
    array.fill(randint(0, 9999))


def MDA_shape(array):
    array.shape


def MDA_3D_set(array, size):
    array[randint(0, size-1), randint(0, size-1), randint(0, size-1)] = randint(0, 9999)


def MDA_3D_get(array, size):
    array[randint(0, size-1), randint(0, size-1), randint(0, size-1)]




size = sizes[0]
@pytest.mark.benchmark(group="2d array size " + str(size))
def test_2d_set(benchmark):
    array = MultiDimensionalArray(int, size, size)
    keyword_args = {'array': array, 'size': size}
    benchmark.pedantic(MDA_2D_set, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="2d array size " + str(size))
def test_2d_get(benchmark):
    array = MultiDimensionalArray(int, size, size)
    keyword_args = {'array': array, 'size': size}
    benchmark.pedantic(MDA_2D_get, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="2d array size " + str(size))
def test_2d_fill(benchmark):
    array = MultiDimensionalArray(int, size, size)
    keyword_args = {'array': array}
    benchmark.pedantic(MDA_fill, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="2d array size " + str(size))
def test_2d_shape(benchmark):
    array = MultiDimensionalArray(int, size, size)
    keyword_args = {'array': array}
    benchmark.pedantic(MDA_shape, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)


size = sizes[1]
@pytest.mark.benchmark(group="2d array size " + str(size))
def test_2d_set2(benchmark):
    array = MultiDimensionalArray(int, size, size)
    keyword_args = {'array': array, 'size': size}
    benchmark.pedantic(MDA_2D_set, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="2d array size " + str(size))
def test_2d_get2(benchmark):
    array = MultiDimensionalArray(int, size, size)
    keyword_args = {'array': array, 'size': size}
    benchmark.pedantic(MDA_2D_get, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="2d array size " + str(size))
def test_2d_fill2(benchmark):
    array = MultiDimensionalArray(int, size, size)
    keyword_args = {'array': array}
    benchmark.pedantic(MDA_fill, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="2d array size " + str(size))
def test_2d_shape2(benchmark):
    array = MultiDimensionalArray(int, size, size)
    keyword_args = {'array': array}
    benchmark.pedantic(MDA_shape, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)


size = sizes[1]
@pytest.mark.benchmark(group="3d array size " + str(size))
def test_3d_set(benchmark):
    array = MultiDimensionalArray(int, size, size, size)
    keyword_args = {'array': array, 'size': size}
    benchmark.pedantic(MDA_3D_set, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="3d array size " + str(size))
def test_3d_get(benchmark):
    array = MultiDimensionalArray(int, size, size, size)
    keyword_args = {'array': array, 'size': size}
    benchmark.pedantic(MDA_3D_get, kwargs=keyword_args, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="3d array size " + str(size))
def test_3d_fill(benchmark):
    array = MultiDimensionalArray(int, size, size, size)
    keyword_args = {'array': array}
    benchmark.pedantic(MDA_fill, kwargs=keyword_args, iterations=1, rounds=20)

@pytest.mark.benchmark(group="3d array size " + str(size))
def test_3d_shape(benchmark):
    array = MultiDimensionalArray(int, size, size, size)
    keyword_args = {'array': array}
    benchmark.pedantic(MDA_shape, kwargs=keyword_args, iterations=1, rounds=20)