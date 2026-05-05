# A palindrome is a number that reads the same backward as forward.
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

print(is_palindrome(121))   # True
print(is_palindrome(123))   # False

# Given an array of integers, move all the zeroes to the end while maintaining the relative order of the non-zero elements.
def move_zeroes(arr):
    pos = 0
    for num in arr:
        if num != 0:
            arr[pos] = num
            pos += 1
    while pos < len(arr):
        arr[pos] = 0
        pos += 1
    return arr

print(move_zeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]

# Given a linked list, find the middle element in one pass.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data  # Middle element

# Build: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(find_middle(head))  # 3

# Stack (LIFO) 
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop() if self.stack else "Empty"
    def peek(self):
        return self.stack[-1] if self.stack else "Empty"

# Queue (FIFO)
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, val):
        self.queue.append(val)
    def dequeue(self):
        return self.queue.pop(0) if self.queue else "Empty"
    def front(self):
        return self.queue[0] if self.queue else "Empty"

s = Stack()
s.push(1); s.push(2); s.push(3)
print(s.pop())   # 3

q = Queue()
q.enqueue(1); q.enqueue(2); q.enqueue(3)
print(q.dequeue())  # 1


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(bubble_sort([64, 34, 25, 12]))     # [12, 25, 34, 64]
print(selection_sort([64, 25, 12, 22]))  # [12, 22, 25, 64]
print(insertion_sort([12, 11, 13, 5]))   # [5, 11, 12, 13]

# Linear Search - O(n)
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Binary Search - O(log n), array must be sorted
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(linear_search([4, 2, 7, 1], 7))        # 2
print(binary_search([1, 3, 5, 7, 9], 7))     # 3


# Tree Traversal: Inorder, Preorder, Postorder
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def inorder(root):    # Left → Root → Right
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def preorder(root):   # Root → Left → Right
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):  # Left → Right → Root
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

#       1
#      / \
#     2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

inorder(root)    # 2 1 3
preorder(root)   # 1 2 3
postorder(root)  # 2 3 1


# Graph Traversal: BFS vs DFS
from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

# BFS - Level by level (uses Queue)
def bfs(start):
    visited, queue = set(), deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# DFS - Go deep first (uses Stack/Recursion)
def dfs(node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

bfs(1)  # 1 2 3 4 5
dfs(1)  # 1 2 4 5 3

# Given a number, return the sum of its digits.
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

print(sum_of_digits(1234))  # 10
print(sum_of_digits(456))   # 15


# Given an array of integers, return the second largest number. If there is no second largest, return None.
def second_max(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None

print(second_max([3, 1, 4, 1, 5, 9, 2, 6]))  # 6
print(second_max([10, 10, 10]))               # None (no distinct second max)

