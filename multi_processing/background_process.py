import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print(name)
    time.sleep(3)
    print("Exiting", name)

if __name__ == "__main__":
    background_process = multiprocessing.Process(name="background_process", target=foo)
    background_process.daemon = True    # to make that process to be executed in background
    NO_background_process = multiprocessing.Process(name="NO_background_process", target=foo)
    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()