import time
import random
from multiprocessing import Process, Pipe, cpu_count, set_start_method

# -----------------------------
# Common merge function
# -----------------------------
def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

# -----------------------------
# Simple merge sort (sequential)
# -----------------------------
def merge_sort_simple(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_simple(arr[:mid])
    right = merge_sort_simple(arr[mid:])
    return merge(left, right)

# -----------------------------
# Multiprocessing merge sort (optimized)
# -----------------------------
def merge_sort_process_top(arr):
    n_cores = cpu_count()
    chunk_size = len(arr) // n_cores
    chunks = [arr[i*chunk_size:(i+1)*chunk_size] for i in range(n_cores-1)]
    chunks.append(arr[(n_cores-1)*chunk_size:])  # last chunk

    pipes = []
    processes = []

    def sort_chunk(chunk, conn):
        conn.send(merge_sort_simple(chunk))
        conn.close()

    # spawn processes
    for chunk in chunks:
        parent_conn, child_conn = Pipe()
        p = Process(target=sort_chunk, args=(chunk, child_conn))
        processes.append(p)
        pipes.append(parent_conn)
        p.start()

    # collect sorted chunks
    sorted_chunks = [pipe.recv() for pipe in pipes]

    # join processes
    for p in processes:
        p.join()

    # sequentially merge all sorted chunks
    result = sorted_chunks[0]
    for i in range(1, len(sorted_chunks)):
        result = merge(result, sorted_chunks[i])

    return result

# -----------------------------
# Benchmark runner
# -----------------------------
if __name__ == "__main__":
    set_start_method("fork")

    N = 5000000
    print("n:", N)
    arr = [random.randint(0, 1_000_000) for _ in range(N)]

    # Sequential
    arr_copy = arr[:]
    start = time.time()
    merge_sort_simple(arr_copy)
    print(f"Simple merge sort time: {time.time() - start:.4f} sec")

    # Multiprocessing (optimized)
    arr_copy = arr[:]
    start = time.time()
    merge_sort_process_top(arr_copy)
    print(f"Multiprocessing merge sort time: {time.time() - start:.4f} sec")
