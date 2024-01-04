class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()
import unittest

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.root = Node(10)
        self.root.insert(6)
        self.root.insert(14)
        self.root.insert(5)
        self.root.insert(8)
        self.root.insert(11)
        self.root.insert(18)

    def test_print_tree(self):
        expected_output = "5 6 8 10 11 14 18"
        result = self.root.print_tree()
        
if __name__ == '__main__':
    unittest.main()
