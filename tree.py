class Node:
    def __init__(self, my_data):
        self.data = my_data
        self.left = None
        self.right = None

def buildTree(self):
    data = input("Enter the data for the node: ")
    root = Node(data)
    if data == "mahi":
        return None
    root.left = self.buildTree()
    root.right = self.buildTree()
    return root

