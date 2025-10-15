import multiprocessing

def foo(i):
    print("called function in process", i)
    

if __name__ == "__main__":
    process_jobs = []
    for i in range(100):
        p = multiprocessing.Process(target=foo, args=(i, ))
        process_jobs.append(p)
        p.start()
        p.join()    # without the join the child process will sit idle and will not be terminated and the we must kill those manually
