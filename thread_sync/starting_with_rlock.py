import threading

'''
lock = threading.Lock()

lock.acquire()
print("Acquired once")
lock.acquire()  # -> results to deadlock
print("Acquired twice")
lock.release()
lock.release()

'''


'''
Therefore, concept of RLock
Reentrant lock: The same thread can acquire it multiple times without blocking itself.
Must be released the same number of times it was acquired before another thread can acquire it.
Use case: When a thread might call a function that also tries to acquire the same lock.
'''
rlock = threading.RLock()

rlock.acquire()
print("Acquired once")
rlock.acquire()
print("Acquired twice")  # No deadlock
rlock.release()
rlock.release()  # Fully released now
