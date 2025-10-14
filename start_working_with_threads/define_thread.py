import threading

def function(i):
    print("Function is Called by Thread", i)
    return

threads = []
for i in range(100):
    t = threading.Thread(target=function, args=(i, ))   # Syntax of Thread: class threading.Thread(group = None, target = None, name = None, args = (), kwargs = {})
    # group: reserverd for future implementations, target: function that is to be executed, name: name of the thread (by default a unique name of the form Thread-N is assigned, args, kwargs)
    threads.append(t)
    t.start()   # launches a new thread of execution at OS level
    t.join()    # join() tells the main thread to wait here untill this particular thread finished before continuing

'''
OUTPUT:
Function is Called by Thread 0
Function is Called by Thread 1
Function is Called by Thread 2
Function is Called by Thread 3
Function is Called by Thread 4
'''