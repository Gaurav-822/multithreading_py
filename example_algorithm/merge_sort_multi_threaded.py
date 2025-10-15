from threading import Thread

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

    res.extend(left[i::])
    res.extend(right[j::])

    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]

    left_sorted = None
    right_sorted = None

    def sort_left():
        nonlocal left_sorted
        left_sorted = merge_sort(left_part)

    def sort_right():
        nonlocal right_sorted
        right_sorted = merge_sort(right_part)

    t1 = Thread(target=sort_left)
    t2 = Thread(target=sort_right)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return merge(left_sorted, right_sorted)

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)