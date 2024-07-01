class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None
def removeDuplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
def print_linked_list(head):
    current_head = head
    while current_head:
        print(int(current_head.data), end=" ")
        if current_head.next:
            print("->", end=" ")
        current_head = current_head.next
    print()
head = None
prev = None
while True:
    try:
        number_str = input("Enter a number (or 'N' to finish): ")
        if number_str.upper() == 'N':
            break
        else:
            number = float(number_str)
            new_node = Node(number)
            if not head or number <= head.data:
                new_node.next = head
                head = new_node
            else:
                current = head
                while current and current.next and current.next.data < number:
                    current = current.next
                new_node.next = current.next
                current.next = new_node
            prev = new_node
    except ValueError:
        print("Invalid input. Please enter a number or 'N' to finish.")
if head is not None:
    print("Original Linked List after sorting: ")
    print_linked_list(head)
    new_head = removeDuplicates(head)
    print("New Linked List after Removing Duplicates: ")
    print_linked_list(new_head)
else:
    print("Linked List is empty")