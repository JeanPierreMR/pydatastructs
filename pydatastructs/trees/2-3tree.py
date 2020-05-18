
class Node:
	def __init__(self, data, par = None):
		self.data = list([data])
		self.parent = par
		self.children = list()
	
	def __lt__(self, node):
		return self.data[0] < node.data[0]
		
	def leaf(self):
		return len(self.children) == 0

	def addNode(self, new_node):
		for children in new_node.children:
			children.parent = self
		self.data.extend(new_node.data)
		self.data.sort()
		self.children.extend(new_node.children)
		if len(self.children) > 1:
			self.children.sort()
		elif len(self.data) > 2:
			self.splitNode()
	
	def insertNode(self, new_node):
		lengthdata = len(self.data)

		if self.leaf():
			self.addNode(new_node)

		elif new_node.data[0] > self.data[-1]:
			self.children[-1].insertNode(new_node)
		else:
			for i in range(0, lengthdata):
				if new_node.data[0] < self.data[i]:
					self.children[i].insertNode(new_node)
					break
	
	def splitNode(self):
		l_children = Node(self.data[0], self)
		r_children = Node(self.data[2], self)
		if self.children:
			l_children.children = [self.children[0], self.children[1]]
			r_children.children = [self.children[2], self.children[3]]
					
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
			
	def findNode(self, item):
 
		if item in self.data:
			return item
		elif self.leaf():
			return False
		elif item > self.data[-1]:
			return self.children[-1].findNode(item)
		else:
			for i in range(len(self.data)):
				if item < self.data[i]:
					return self.children[i].findNode(item)
		
	# Traversal1		
	def preorderTraversal(self):
		for children in self.children:
			children.preorderTraversal()
	
class Tree:
	def __init__(self):
		self.root = None
		
	def insert(self, item):
		print("Inserting: " + str(item))
		if self.root is None:
			self.root = Node(item)
		else:
			self.root.insertNode(Node(item))
			while self.root.parent:
				self.root = self.root.parent
		return True
	
	def find(self, item):
		return self.root.findNode(item)
		
	def remove(self, item):
		self.root.remove(item)
		
		
tree = Tree()

lst = [13, 7, 24, 15, 4, 29, 20, 16, 19, 1, 5, 22, 17]
for item in lst:
	tree.insert(item)














































































    #fuente: https://github.com/joeyajames/Python/blob/master/Trees/2-3_tree.py