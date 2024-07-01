import threading

# Define a shared resource
shared_resource = 0

# Define a lock
lock = threading.Lock()

# Function to increment the shared resource
def increment():
    global shared_resource
    for _ in range(1000000):
        # Acquire the lock before accessing the shared resource
        lock.acquire()
        shared_resource += 1
        # Release the lock after accessing the shared resource
        lock.release()

# Function to decrement the shared resource
def decrement():
    global shared_resource
    for _ in range(1000000):
        # Acquire the lock before accessing the shared resource
        lock.acquire()
        shared_resource -= 1
        # Release the lock after accessing the shared resource
        lock.release()

# Create two threads to increment and decrement the shared resource
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=decrement)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Print the final value of the shared resource
print("Final value of shared resource:", shared_resource)