from pydatastructs import Trie
import string
import random
from time import sleep

size = 100000

def random_word(length):
    length = length + random.choice([1,2,3])
    return ''.join(random.choice(string.ascii_letters) for x in range(length))


def random_words(chars, size):
    words = []
    for x in range(size):
        words.append(random_word(chars))
    return words

def test_trie(size):
    trie = Trie()
    sleep(3)
    for x in range(int(size/2)):
        trie.insert(random_word(20))
    sleep(3)
    for x in range(int(size/2)):
        trie.insert(random_word(20))
    sleep(3)
    for x in range(int(size/10)):
        trie.search(random_word(20))
    sleep(3)
    for x in range(int(size/10)):
        trie.delete(random_word(20))
    sleep(2)



test_trie(size)