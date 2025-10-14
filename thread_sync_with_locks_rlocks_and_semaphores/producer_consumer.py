import threading
import time
import random

buffer = []  # shared space
buffer_size = 5  # maximum buffer capacity

# Semaphore to track available items
items = threading.Semaphore(0)
# Semaphore to track free slots in buffer
spaces = threading.Semaphore(buffer_size)
# Lock to protect buffer access
buffer_lock = threading.Lock()

def consumer(consumer_id):
    while True:
        items.acquire()  # wait until an item is available
        with buffer_lock:
            item = buffer.pop(0)  # consume the item
            print(f"Consumer {consumer_id} consumed item: {item}")
        spaces.release()  # signal a free space
        time.sleep(random.uniform(0.5, 2))  # simulate consumption time

def producer(producer_id):
    while True:
        item = random.randint(0, 1000)
        spaces.acquire()  # wait until there is space
        with buffer_lock:
            buffer.append(item)  # produce the item
            print(f"Producer {producer_id} produced item: {item}")
        items.release()  # signal an available item
        time.sleep(random.uniform(0.5, 2))  # simulate production time

if __name__ == "__main__":
    # Create multiple producers and consumers
    producers = [threading.Thread(target=producer, args=(i,)) for i in range(3)]
    consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(2)]

    for t in producers + consumers:
        t.daemon = True  # allows program to exit even if threads are running
        t.start()

    # Let the simulation run for 15 seconds
    time.sleep(5)

    print("Program terminated")
