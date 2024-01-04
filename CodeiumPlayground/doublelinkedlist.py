class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print()


# Use the DoublyLinkedList
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()  # Output: 1 2 3
