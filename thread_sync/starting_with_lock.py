import threading

shared_resource_with_lock = 0
shared_resource_with_no_lock = 0

COUNT = 10

lock = threading.Lock()  # separate variable for lock

# LOCK Management
def increment_with_lock():
    global shared_resource_with_lock
    for _ in range(COUNT):
        with lock:
            shared_resource_with_lock += 1

def decrement_with_lock():
    global shared_resource_with_lock
    for _ in range(COUNT):
        with lock:
            shared_resource_with_lock -= 1

# NO LOCK Management
def increment_without_lock():
    global shared_resource_with_no_lock
    for _ in range(COUNT):
        shared_resource_with_no_lock += 1
        

def decrement_without_lock():
    global shared_resource_with_no_lock
    for _ in range(COUNT):
        shared_resource_with_no_lock -= 1

t1 = threading.Thread(target=increment_with_lock)
t2 = threading.Thread(target=decrement_with_lock)
t3 = threading.Thread(target=increment_without_lock)
t4 = threading.Thread(target=decrement_without_lock)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print("With Lock:", shared_resource_with_lock)
print("Without Lock:", shared_resource_with_no_lock)


