import threading
import time

class Box():
    lock = threading.RLock()
    def __init__(self):
        self.total_items = 0
    
    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()
    
    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()
    
    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()

## this 2 functions run n in seperate threads and call the Box's method
def adder(box, items):
    while items > 0:
        print("Adding 1 item in the box")
        box.add()
        time.sleep(5)
        items -= 1

def remover(box, items):
    while items > 0:
        print("removing 1 item from the box")
        box.remove()
        time.sleep(5)
        items -= 1


if __name__ == "__main__":
    items = 5
    print(f"Putting {items} in the box")
    box = Box()
    t1 = threading.Thread(target = adder, args = (box, items))
    t2 = threading.Thread(target = remover, args = (box, items))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"{box.total_items} items still remain in the box")