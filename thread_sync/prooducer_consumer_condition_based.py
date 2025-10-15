from threading import Thread, Condition

items = []
condition = Condition() # the shared resource items is modeled through condition, (By default this uses RLock)

class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def consume(self):
        global condition
        global items

        condition.acquire()

        if len(items) == 0:
            condition.wait()
            print("Consumer notify: No item to consume")
        
        items.pop()
        print("Consumer notify: Consumed 1 item")
        print("Items Left:", len(items))
        
        condition.notify()
        condition.release()
    
    def run(self):
        for i in range(20):
            self.consume()
    
class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items

        condition.acquire()

        if len(items) ==  10:
            condition.wait()
            print("Producer Notify: max level reached, can't produce more")
        
        items.append(1)
        print("Producer Notify: Added 1 item")
        print("Items Left:", len(items))

        condition.notify()
        condition.release()

    def run(self):
        for i in range(20):
            self.produce()

if __name__ == "__main__":
    producer = Producer()
    consumer = Consumer()

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()