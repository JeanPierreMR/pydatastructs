from pydatastructs.utils import MAryTreeNode
from pydatastructs.linear_data_structures.arrays import ArrayForTrees

__all__ = [
    'MAryTree',
    'Tree2_4'
]

class MAryTree(object):
    """
    Abstract m-ary tree.

    Parameters
    ==========

    key
        Required if tree is to be instantiated with
        root otherwise not needed.

    root_data
        Optional, the root node of the binary tree.
        If not of type MAryTreeNode, it will consider
        root as data and a new root node will
        be created.

    comp: lambda
        Optional, A lambda function which will be used
        for comparison of keys. Should return a
        bool value. By default it implements less
        than operator.

    is_order_statistic: bool
        Set it to True, if you want to use the
        order statistic features of the tree.

    max_children
        Optional, specifies the maximum number of children
        a node can have. Defaults to 2 in case nothing is
        specified.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/M-ary_tree
    """

    __slots__ = ['root_idx', 'max_children', 'comparator', 'tree', 'size',
                 'is_order_statistic']


    def __new__(cls, key=None, root_data=None, comp=None,
                is_order_statistic=False, max_children=2):
        obj = object.__new__(cls)
        if key is None and root_data is not None:
            raise ValueError('Key required.')
        key = None if root_data is None else key
        root = MAryTreeNode(key, root_data)
        root.is_root = True
        obj.root_idx = 0
        obj.max_children = max_children
        obj.tree, obj.size = ArrayForTrees(MAryTreeNode, [root]), 1
        obj.comparator = lambda key1, key2: key1 < key2 \
                        if comp is None else comp
        obj.is_order_statistic = is_order_statistic
        return obj

    @classmethod
    def methods(cls):
        return ['__new__', '__str__']

    def insert(self, key, data=None):
        """
        Inserts data by the passed key using iterative
        algorithm.

        Parameters
        ==========

        key
            The key for comparison.

        data
            The data to be inserted.

        Returns
        =======

        None
        """
        raise NotImplementedError("This is an abstract method.")

    def delete(self, key, **kwargs):
        """
        Deletes the data with the passed key
        using iterative algorithm.

        Parameters
        ==========

        key
            The key of the node which is
            to be deleted.

        Returns
        =======

        True
            If the node is deleted successfully.

        None
            If the node to be deleted doesn't exists.

        Note
        ====

        The node is deleted means that the connection to that
        node are removed but the it is still in tree.
        """
        raise NotImplementedError("This is an abstract method.")

    def search(self, key, **kwargs):
        """
        Searches for the data in the binary search tree
        using iterative algorithm.

        Parameters
        ==========

        key
            The key for searching.

        parent: bool
            If true then returns index of the
            parent of the node with the passed
            key.
            By default, False

        Returns
        =======

        int
            If the node with the passed key is
            in the tree.
        tuple
            The index of the searched node and
            the index of the parent of that node.
        None
            In all other cases.
        """
        raise NotImplementedError("This is an abstract method.")

    def to_binary_tree(self):
        """
        Converts an m-ary tree to a binary tree.

        Returns
        =======

        TreeNode
            The root of the newly created binary tree.
        """
        raise NotImplementedError("This is an abstract method.")


    def __str__(self):
        to_be_printed = ['' for i in range(self.tree._last_pos_filled + 1)]
        for i in range(self.tree._last_pos_filled + 1):
            if self.tree[i] is not None:
                node = self.tree[i]
                to_be_printed[i] = (node.key, node.data)
                for j in node.children:
                    if j is not None:
                        to_be_printed[i].append(j)
        return str(to_be_printed)


class Node2_4:
    def __init__(self, data, par=None):
        self.data = list([data])
        self.parent = par
        self.children = list()

    def __lt__(self, node):
        return self.data[0] < node.data[0]

    def leaf(self):
        length = len(self.children)
        return length == 0

    def addNode(self, new_node):
        for children in new_node.children:
            children.parent = self
        self.data.extend(new_node.data)
        self.data.sort()

        self.children.extend(new_node.children)
        if len(self.children) > 1:
            self.children.sort()
        elif len(self.data) > 3:
            self.splitNode()

    def insertNode(self, new_node):
        lengthdata = len(self.data)
        new_nodedata = new_node.data[0]

        if self.leaf():
            self.addNode(new_node)

        elif new_nodedata > self.data[-1]:
            self.children[-1].insertNode(new_node)

        else:
            for i in range(0, lengthdata):
                if new_nodedata < self.data[i]:
                    self.children[i].insertNode(new_node)
                    break

    def splitNode(self):
        print("Node split: " + str(self.data))

        l_children = Node2_4(self.data[0], self)
        r_children = Node2_4(self.data[2], self)
        r_children.data.append(self.data[3])

        if self.children:
            l_children.children = [self.children[0], self.children[1]]
            r_children.children = [self.children[2], self.children[3], self.children[4]]

        self.children = [l_children]
        self.children.append(r_children)
        self.data = [self.data[1]]

        if self.parent:
            if self in self.parent.children:
                self.parent.children.remove(self)
            self.parent.addNode(self)
        else:
            l_children.parent = self
            r_children.parent = self

    def findNode(self, key):
        lengthdata = len(self.data)

        if key in self.data:
            return key

        elif self.leaf():
            return False

        elif key > self.data[-1]:
            return self.children[-1].findNode(key)

        else:
            for i in range(lengthdata):
                if key < self.data[i]:
                    return self.children[i].findNode(key)

    def preorderTranversal(self):
        for children in self.children:
            children.preorderTranversal()


class Tree2_4:
    def __init__(self):
        self.root = None

    def insert(self, key):
        print("Inserting: " + str(key))
        if self.root is None:
            self.root = Node2_4(key)
        else:
            self.root.insertNode(Node2_4(key))
            while self.root.parent:
                self.root = self.root.parent
        return True

    def find(self, item):
        return self.root.findNode(item)

    def traverse(self):
        thislevel = [self.root]
        while thislevel:
            nextlevel = list()
            print('\n')
            for n in thislevel:
                print(str(n.data), end=' ')
                for children in n.children:
                    nextlevel.append(children)
                thislevel = nextlevel