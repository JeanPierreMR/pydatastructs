import pickle
from pydatastructs import MultiDimensionalArray, Trie, SparseTable, Tree2_4
def save_object(obj, filename):
    with open(filename, 'wb+') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def load_object(filename):
    with open(filename, 'rb') as input:
        return pickle.load(input)

def creation():
    multi_array = MultiDimensionalArray(int, 5, 9, 3, 8)
    multi_array.fill(6)

    trie = Trie()
    trie.insert("hi")
    trie.insert("search")
    trie.insert("sea")
    trie.insert("see")

    tree = Tree2_4()
    numbers = [7, 4, 2, 1, 6]
    for x in numbers:
        tree.insert(x)

    st = SparseTable([0, 1, 2, 3, 4, 5])
    return multi_array, trie, tree, st


def do_task():
    try:
        print(multi_array[0, 0, 0, 0] == 6)
        print("array existe")
    except:
        print("array no existe")
    try:
        print(trie.search("hi"))
        print("trie existe")
    except:
        print("trie no existe")
    try:
        print(tree.find(7) == 7)
        print("tree existe")
    except:
        print("tree no existe")
    try:
        print(st.query(0, 1) == 0)
        print("st existe")
    except:
        print("st no existe")

multi_array, trie, tree, st = creation()

#Saving objects
save_object(multi_array.get_state(), 'marr.pkl')
save_object(trie, 'trie.pkl')
save_object(tree, 'tree24.pkl')
save_object(st, 'st.pkl')


del multi_array
del trie
del tree
del st

do_task()

state_MDA = load_object('marr.pkl')
multi_array = MultiDimensionalArray(state_MDA['dtype'], state_MDA['sizes'], state_MDA['data'])
trie = load_object('trie.pkl')
tree = load_object('tree24.pkl')
st = load_object('st.pkl')

do_task()