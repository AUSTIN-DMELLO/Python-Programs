from collections import deque
def sort_queue(q):
    n = len(q)
    for i in range(n):
        min_index = find_min_index(q, n - i)
        move_min_to_rear(q, min_index)
def find_min_index(q, sort_index):
    min_val = float('inf')
    min_index = -1
    for i, item in enumerate(q):
        if i < sort_index and item < min_val:
            min_val = item
            min_index = i
    return min_index
def move_min_to_rear(q, min_index):
    min_val = None
    n = len(q)
    for i in range(n):
        current = q.popleft()
        if i != min_index:
            q.append(current)
        else:
            min_val = current
    q.append(min_val)
queue = deque()
num_items = int(input("Enter the number of numbers in the queue: "))
for _ in range(num_items):
    item = int(input("Enter number: "))
    queue.append(item)
sort_queue(queue)
print("Sorted Queue (ascending order):", list(queue))