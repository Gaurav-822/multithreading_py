# On the producer and consumer problem
import multiprocessing
import random
import time

class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
    
    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f"Process Producer: item {item}, appended to queue {self.name}")

class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
    
    def run(self):
        while True:
            if (self.queue.empty()):
                print("Queue is Empty")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print(f"Process Consumer: item {item}, popped from queue {self.name}")
                time.sleep(1)

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    process_producer = producer(queue)
    process_consumer = consumer(queue)

    process_producer.start()
    process_consumer.start()

    process_producer.join()
    process_consumer.join()