import pytest
from pydatastructs import Trie
from random import randint
from random_words import RandomWords

trie = Trie()
rw = RandomWords()
sizes = [10, 1000]
n_iterations = 100
n_rounds = 50

#decorators
def random_words(*dec_args, **dec_kwargs):
    '''decorador lista de palabras aleatorias'''
    def _random_words(func):
        def inner(*args, **kwargs):
            rand_words = rw.random_words(count=size)
            return func(rand_words, *args, **kwargs)
        return inner
    return _random_words(dec_args[0])


def random_trie(*dec_args, **dec_kwargs):
    '''decorador lista de palabras aleatorias'''
    def _random_trie(func):
        def inner(*args, **kwargs):
            trie_tree = Trie()
            words = rw.random_words(count=size)
            for word in words:
                trie.insert(word)
            return func(trie_tree, words, *args, **kwargs)
        return inner
    return _random_trie(dec_args[0])


#functions
@random_trie
def trie_insert(trie, words):
    trie.insert(words[randint(0, size - 1)])

@random_trie
def trie_search(trie, words):
    trie.search(rw.random_word())

@random_trie
def trie_delete(trie, words):
    trie.delete(words[randint(0, size - 1)])

@random_words
def trie_profiling_instructions(words):
    # words = rw.random_words(count=size1)
    trie = Trie()
    n = size
    for word in words:
        trie.insert(word)
    trie.search(words[randint(0, n - 1)])
    trie.delete(words.pop(randint(0, n - 1)))

size = sizes[0]
@pytest.mark.benchmark(group="Trie size " + str(size))
def test_trie_general(benchmark):
    benchmark.pedantic(trie_profiling_instructions, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Trie size " + str(size))
def test_trie_insert(benchmark):
    benchmark.pedantic(trie_insert, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Trie size " + str(size))
def test_trie_search(benchmark):
    benchmark.pedantic(trie_search, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Trie size " + str(size))
def test_trie_delete(benchmark):
    benchmark.pedantic(trie_delete, iterations=n_iterations, rounds=n_rounds)


size = sizes[1]
@pytest.mark.benchmark(group="Trie size " + str(size))
def test_trie_insert2(benchmark):
    benchmark.pedantic(trie_insert, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Trie size " + str(size))
def test_trie_search2(benchmark):
    benchmark.pedantic(trie_search, iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Trie size " + str(size))
def test_trie_delete2(benchmark):
    benchmark.pedantic(trie_delete, iterations=n_iterations, rounds=n_rounds)