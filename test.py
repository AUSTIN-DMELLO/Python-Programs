class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def create_linked_list_from_user_input():
    head = None
    prev = None 
    while True:
        try:
            number_str = input("Enter a number (or 'N' to finish): ")
            if number_str.upper() == 'N':
                break  
            number = float(number_str)  
            new_node = Node(number)
            if not head or number <= head.data:
                new_node.next = head
                head = new_node
            else:
                while prev and prev.next and prev.next.data < number:
                    prev = prev.next
                new_node.next = prev.next
                prev.next = new_node
            prev = new_node

        except ValueError:
            print("Invalid input. Please enter a number or 'N' to finish.")

    return head

def remove_duplicates(head):

    if not head:
        return head

    current = head
    prev = None

    while current:
        if prev and prev.data == current.data:
            prev.next = current.next
        else:
            prev = current
        current = current.next

    return head

head = create_linked_list_from_user_input()

if head:
    modified_head = remove_duplicates(head)

    while modified_head:
        print(modified_head.data)
        modified_head = modified_head.next
    print("None")
else:
    print("Null")
