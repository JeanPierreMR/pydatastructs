from pydatastructs import Tree2_4
from random import randint
from time import sleep

size = 100000

def random_number():
    return randint(-99999999, 99999999)

def test_trie(size):
    tree = Tree2_4()
    sleep(3)
    for x in range(int(size/2)):
        tree.insert(random_number())
    sleep(3)
    for x in range(int(size/2)):
        tree.insert(random_number())
    sleep(2)



test_trie(size)