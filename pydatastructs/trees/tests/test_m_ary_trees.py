from pydatastructs import MAryTree, Tree2_4

def test_MAryTree():
    m = MAryTree(1, 1)
    assert str(m) == '[(1, 1)]'

#Example shown below:
#lst = [3, 1, 5, 4, 2, 9, 10, 8, 7, 6]
#for item in lst:
#    tree.insert(item)
#tree.traverse()
def test_tree2_4():
    tree = Tree2_4()
    numbers = [7, 4, 2, 1, 6]
    for x in numbers:
        tree.insert(x)
    assert tree.find(7) == 7
    assert tree.find(1) == 1
    assert tree.find(4) == 4
    assert tree.find(6) == 6
    assert tree.find(31) == False
