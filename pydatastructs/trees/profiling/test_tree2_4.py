import pytest
from pydatastructs import Tree2_4
from random import randint

sizes = [10, 10000]
n_iterations = 10
n_rounds = 100


def random_number():
    return randint(-9999999, 9999999)

def random_tree():
    tree = Tree2_4()
    for x in range(size):
        tree.insert(random_number())
    keyword_args = {'tree': tree}
    return keyword_args


#functions
def tree_insert(tree: Tree2_4):
    tree.insert(random_number())


def tree_search(tree: Tree2_4):
    tree.find(random_number())



size = sizes[0]
@pytest.mark.benchmark(group="Tree size " + str(size))
def test_tree_insert(benchmark):
    benchmark.pedantic(tree_insert, kwargs=random_tree(), iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Tree size " + str(size))
def test_tree_search(benchmark):
    benchmark.pedantic(tree_search, kwargs=random_tree(), iterations=n_iterations, rounds=n_rounds)



size = sizes[1]
@pytest.mark.benchmark(group="Tree size " + str(size))
def test_tree_insert2(benchmark):
    benchmark.pedantic(tree_insert, kwargs=random_tree(), iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Tree size " + str(size))
def test_tree_search2(benchmark):
    benchmark.pedantic(tree_search, kwargs=random_tree(), iterations=n_iterations, rounds=n_rounds)