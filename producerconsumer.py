import threading
import queue
import time
import random

# Define a shared queue with a maximum size
q = queue.Queue(maxsize=5)

# Define a function for the producer
def producer():
    while True:
        item = random.randint(1, 100)  # Generate a random item
        q.put(item)  # Put the item into the queue
        print("Produced:", item)
        time.sleep(random.random())  # Simulate some processing time

# Define a function for the consumer
def consumer():
    while True:
        item = q.get()  # Get an item from the queue
        print("Consumed:", item)
        q.task_done()  # Indicate that the task is complete
        time.sleep(random.random())  # Simulate some processing time

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start both threads
producer_thread.start()
consumer_thread.start()

# Wait for both threads to finish
producer_thread.join()
consumer_thread.join()