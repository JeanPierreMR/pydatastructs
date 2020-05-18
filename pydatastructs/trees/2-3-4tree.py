class Node:
    def __init__(self, data, par = None):
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
        lengthdata  = len(self.data)
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
        l_children = Node(self.data[0], self)
        r_children = Node(self.data[2], self)
        r_children.data.append(self.data[3])

        if self.children:
            l_children.children = [self.children[0], self.children[1]]
            r_children.children = [self.children[2], self.children[3],self.children[4]]
                    
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
        if self.root is None:
            self.root = Node(key)
        else:
            self.root.insertNode(Node(key))
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
                print (str(n.data), end=' ')
                for children in n.children:
                    nextlevel.append(children)
                thislevel = nextlevel



#Example shown below:
#lst = [3, 1, 5, 4, 2, 9, 10, 8, 7, 6]
#for item in lst:
#    tree.insert(item)
#tree.traverse()