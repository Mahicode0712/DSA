class Node:
    def __init__(self, nodeData):
        self.data = nodeData
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def buildTree(self):
        data = int(input("Apne node ki value btaye : "))
        if data == -1:
            return None
        
        node = Node(data)

        print("Left child ka naam btaye, aapke papa : ", data)
        node.left = self.buildTree()

        print("Left child ka naam btaye, aapke papa : ", data)
        node.right = self.buildTree()

        return node
    
    def inorder(self, myRoot):
        if myRoot == None:          # Base condition
            return 
        
        self.postOrder(myRoot.left)  # Visiting left child (L)
        print(myRoot.data, end=" ") # Printing current Node (N)
        self.postOrder(myRoot.right) # Visiting right child (R)

    def levelOrderTraversal(self, myRoot):
        if myRoot == None:
            return
        
        queue = []
        queue.append(myRoot)
        queue.append(None)
        print()
        while(queue):
            root = queue[0]
            queue.pop(0)
            if root == None:
                print()
                if queue:
                    queue.append(None)

            else:
                print(root.data, end=" ")
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                
    def preOrder(self, myRoot):
        if myRoot == None:          # Base condition
            return 
        
        print(myRoot.data, end=" ") # Printing current Node (N)
        self.preOrder(myRoot.left)  # Visiting left child (L)
        self.preOrder(myRoot.right) # Visiting right child (R)

    def postOrder(self, myRoot):
        if myRoot == None:          # Base condition
            return 
        
        self.postOrder(myRoot.left)  # Visiting left child (L)
        self.postOrder(myRoot.right) # Visiting right child (R)
        print(myRoot.data, end=" ") # Printing current Node (N)

    
myBinaryTree = BinaryTree()
meraRoot = myBinaryTree.buildTree()
myBinaryTree.inorder(meraRoot)
myBinaryTree.preOrder(meraRoot)
myBinaryTree.postOrder(meraRoot)
myBinaryTree.levelOrderTraversal(meraRoot)