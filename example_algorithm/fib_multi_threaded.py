import threading
import time

# normal algo
def fib(n):
    if n <= 1:
        return n
    
    x = fib(n - 1)
    y = fib(n - 2)

    return x + y

def multi_threaded_fib(n):
    if n <= 1:
        return n
    
    result = [None, None]

    def compute_first():
        result[0] = multi_threaded_fib(n - 1)
    def compute_sec():
        result[1] = multi_threaded_fib(n - 2)

    t1 = threading.Thread(target=compute_first)
    t2 = threading.Thread(target=compute_sec)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return result[0] + result[1]



# Measure time for normal fib
start = time.time()
normal_result = fib(10)
end = time.time()
print(f"Normal fib(5) = {normal_result}, Time = {end - start:.6f} seconds")

# Measure time for multi-threaded fib
start = time.time()
threaded_result = multi_threaded_fib(10)
end = time.time()
print(f"Multi-threaded fib(5) = {threaded_result}, Time = {end - start:.6f} seconds")