from collections import deque

class LinkedListDeque:
    def __init__(self):
        self.llist = deque()

    def append(self, data):
        self.llist.append(data)

    def remove_first(self):
        if self.llist:
            return self.llist.popleft()
        else:
            return None

    def traverse(self):
        for item in self.llist:
            print(item, end=" ")
        print()

ll_deque = LinkedListDeque()
num_nodes = int(input("Enter the number of nodes: "))
for _ in range(num_nodes):
    data = int(input("Enter data for node: "))
    ll_deque.append(data)

removed_item = ll_deque.remove_first()
print("Removed item:", removed_item)

print("Linked list contents:")
ll_deque.traverse()
