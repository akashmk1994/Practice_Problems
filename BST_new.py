class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, element):
        if self.data == element:
            print("Found")
            return self.data
        if self.left and self.data > element:
            return self.left.search(element)
        if self.right and self.data < element:
            return self.right.search(element)
        print("Value not in Tree")

    def traverse_preorder(self):
        print(self.data)
        if self.left:
            self.left.traverse_preorder()
        if self.right:
            self.right.traverse_preorder()

    def traverse_inorder(self):
        if self.left:
            self.left.traverse_inorder()
        print(self.data)
        if self.right:
            self.right.traverse_inorder()

    def traverse_postorder(self):
        if self.left:
            self.left.traverse_postorder()
        if self.right:
            self.right.traverse_postorder()
        print(self.data)


class Tree:
    def __init__(self, root, name):
        self.root = root
        self.name = name

    def search(self, element):
        return self.root.search(element)

    def traverse_preorder(self):
        self.root.traverse_preorder()

    def traverse_inorder(self):
        self.root.traverse_inorder()

    def traverse_postorder(self):
        self.root.traverse_postorder()


# node = Node(10)
# node.left = Node(5)
# node.right = Node(15)
# node.left.left = Node(4)
# node.left.right = Node(16)
# node.right.left = Node(3)
# node.right.right = Node(26)

# print(node.data)

myTree = Tree(Node(50), 'Tree Traversal')
myTree.root.left = Node(25)
myTree.root.right = Node(75)
myTree.root.left.left = Node(10)
myTree.root.left.right = Node(35)
myTree.root.left.right.left = Node(30)
myTree.root.left.right.right = Node(42)
myTree.root.left.left.left = Node(5)
myTree.root.left.left.right = Node(13)

# print(myTree.name)
# print(myTree.root.right.left.data)
# print(myTree.root.right.data)
# found = myTree.search(26)
print("PreOrder Traversal")
myTree.traverse_preorder()
print("InOrder Traversal")
myTree.traverse_inorder()
print("PostOrder Traversal")
myTree.traverse_postorder()