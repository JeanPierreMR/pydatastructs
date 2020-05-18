from pydatastructs import MultiDimensionalArray
import string
import random
from time import sleep

size = 1000


def random_word(length=20):
    length = length + random.choice([1, 2, 3])
    return ''.join(random.choice(string.ascii_letters) for x in range(length))


def random_words(chars, size):
    words = []
    for x in range(size):
        words.append(random_word(chars))
    return words


def test_trie(size):
    # 2 dimensions int
    array = MultiDimensionalArray(int, size, size)
    sleep(3)
    for x in range(size):
        for y in range(size):
            array[x][y] = random.randint(-99000, 99000)
    sleep(3)
    array.fill(4000)
    sleep(3)
    # 2 dimensions String
    array = MultiDimensionalArray(str, size, 2*size)
    sleep(3)
    for x in range(size):
        for y in range(size):
            array[x][y] = random_word()
    sleep(3)
    array.fill("Veritas")
    sleep(3)
    # 3 dimensions String
    array = MultiDimensionalArray(str, size, size, 20)
    sleep(3)
    for x in range(size):
        for y in range(size):
            for z in range(19):
                array[x][y][z] = random_word()
    sleep(3)
    array.fill("Libertas")
    sleep(3)


test_trie(size)
