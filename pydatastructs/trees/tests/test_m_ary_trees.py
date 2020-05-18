from pydatastructs import MAryTree, Trie, Tree2_4

def test_MAryTree():
    m = MAryTree(1, 1)
    assert str(m) == '[(1, 1)]'

def test_trie():
    trie = Trie()
    trie.insert("hi")
    trie.insert("search")
    trie.insert("sea")
    trie.insert("see")
    trie.insert("seek")
    assert trie.search("Bonjour") == False
    assert trie.search("see")
    assert trie.search("sew").sort() == ["search", "sea", "see", "seek"].sort()
    trie.delete("see")
    assert trie.search("see").sort() == ["search", "sea", "seek"].sort()
    assert trie.search("sea")

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
