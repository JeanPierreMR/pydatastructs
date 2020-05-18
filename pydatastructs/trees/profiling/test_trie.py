import pytest
from pydatastructs import Trie
from random import randint, choice
import string
trie = Trie()
sizes = [10, 10000]
word_lengths = [20, 40]
n_iterations = 100
n_rounds = 1000


def random_word(length=20):
    length = length + choice([1, 2, 3])
    return ''.join(choice(string.ascii_letters) for x in range(length))


def random_words(size, length=20):
    words = []
    for x in range(size):
        words.append(random_word(length))
    return words


def random_trie(word_length=20):
    trie_tree = Trie()
    words = random_words(size=size, length=word_length)
    for word in words:
        trie.insert(word)
    keyword_args = {'trie': trie_tree, 'words': words}
    return keyword_args


#functions
def trie_insert(trie, words):
    trie.insert(words[randint(0, size - 1)])


def trie_search(trie, words):
    trie.search(words[randint(0, size - 1)])


def trie_delete(trie, words):
    trie.delete(words[randint(0, size - 1)])


word_length = word_lengths[0]
size = sizes[0]
@pytest.mark.benchmark(group="Trie size " + str(size) + " word length " + str(word_length))
def test_trie_insert(benchmark):
    benchmark.pedantic(trie_insert, kwargs=random_trie(), iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Trie size " + str(size) + " word length " + str(word_length))
def test_trie_search(benchmark):
    benchmark.pedantic(trie_search, kwargs=random_trie(), iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Trie size " + str(size) + " word length " + str(word_length))
def test_trie_delete(benchmark):
    benchmark.pedantic(trie_delete, kwargs=random_trie(), iterations=n_iterations, rounds=n_rounds)


size = sizes[1]
@pytest.mark.benchmark(group="Trie size " + str(size) + "word length " + str(word_length))
def test_trie_insert2(benchmark):
    benchmark.pedantic(trie_insert, kwargs=random_trie(), iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Trie size " + str(size) + "word length " + str(word_length))
def test_trie_search2(benchmark):
    benchmark.pedantic(trie_search, kwargs=random_trie(), iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Trie size " + str(size) + "word length " + str(word_length))
def test_trie_delete2(benchmark):
    benchmark.pedantic(trie_delete, kwargs=random_trie(), iterations=n_iterations, rounds=n_rounds)


word_length = word_lengths[1]
size = sizes[1]
@pytest.mark.benchmark(group="Trie size " + str(size) + " word length " + str(word_length))
def test_trie_insert3(benchmark):
    benchmark.pedantic(trie_insert, kwargs=random_trie(), iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Trie size " + str(size) + " word length " + str(word_length))
def test_trie_search3(benchmark):
    benchmark.pedantic(trie_search, kwargs=random_trie(), iterations=n_iterations, rounds=n_rounds)

@pytest.mark.benchmark(group="Trie size " + str(size) + " word length " + str(word_length))
def test_trie_delete3(benchmark):
    benchmark.pedantic(trie_delete, kwargs=random_trie(), iterations=n_iterations, rounds=n_rounds)