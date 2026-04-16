# Doubly Linked List Implementation in Python
class Node:
    def __init__(self,my_data):
        self.data = my_data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_firstposition(self,my_data):
        new_node = Node(my_data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def traversal(self):
     curNode = self.head
     while curNode != None:
      print(curNode.data , end="->")
      curNode = curNode.next

dll = DoublyLinkedList()
dll.insert_at_firstposition("Shayam")
dll.insert_at_firstposition("Vikram")
dll.insert_at_firstposition("Karan")
dll.traversal()

#insert at last position
def insert_at_lastposition(self,my_data):
    curNode = Node(my_data)
    if self.head == None:
        self.head = curNode
    else:
        curNode = self.head
        while curNode.next != None: 
            curNode = curNode.next
        curNode.next = curNode
        curNode.prev = curNode

#insert at any position
def insert_at_anyposition(self,my_data,position):
    curNode = Node(my_data)
    if self.head == None:
        curNode = self.head
    curNode.next = curNode
    curNode.prev = curNode
        