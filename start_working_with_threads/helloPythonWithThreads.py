from threading import Thread
from time import sleep

# create a thread in python, we will want to make our class work as a thread
class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = "Hello Parallel Python Cookbook!!\n"
    
    def print_message(self):
        print(self.message)
    
    def run(self):
        print("Thread is Starting \n")
        for _ in range(10):
            self.print_message()
            sleep(2)
        print("Thread Ended \n")

print("Process Started")
hello_python = CookBook()
hello_python.start()
print("Process Ended!")

# Therefore Threads are a subtask doing something in a parent process