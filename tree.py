class Node:
    def __init__(self, my_data):
        self.data = my_data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def buildTree(self):

        
        data = int(input("Enter the data for the node: "))
        
        node = Node(data) 

        print("Enter the left child of", data)
        node.left = self.buildTree()

        print("Enter the right child of", data) 
        node.right = self.buildTree()  
        return node

MyBinaryTree = BinaryTree()
Root = MyBinaryTree.buildTree()