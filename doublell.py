class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_after(self, key, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == key:
                next_node = current.next
                current.next = new_node
                new_node.prev = current
                new_node.next = next_node
                if next_node:
                    next_node.prev = new_node
                break
            current = current.next

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def traverse_backward(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

dll = DoublyLinkedList()
num_nodes = int(input("Enter the number of nodes: "))
for _ in range(num_nodes):
    data = int(input("Enter data for node: "))
    dll.append(data)

key = int(input("Enter the key after which to insert a new node: "))
data = int(input("Enter data for the new node: "))
dll.insert_after(key, data)

print("Forward traversal:")
dll.traverse_forward()
print("Backward traversal:")
dll.traverse_backward()
