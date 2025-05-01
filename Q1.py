import threading
import random
import time

# Normal Single-threaded Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merging the sorted halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Multi-threaded Merge Sort
def threaded_merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Create two threads
    t1 = threading.Thread(target=threaded_merge_sort, args=(left,))
    t2 = threading.Thread(target=threaded_merge_sort, args=(right,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    i = j = k = 0

    # Merging the sorted halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Function to measure time
def measure_time(sort_function, arr):
    start = time.time()
    sort_function(arr)
    end = time.time()
    return end - start

# Main program
if __name__ == "__main__":
    # Create a random list
    size = 10000
    arr = [random.randint(0, 100000) for _ in range(size)]
    arr_copy = arr.copy()

    # Single-threaded
    time_single = measure_time(merge_sort, arr)
    print(f"Single-threaded Merge Sort Time: {time_single:.4f} seconds")

    # Multi-threaded
    time_threaded = measure_time(threaded_merge_sort, arr_copy)
    print(f"Multi-threaded Merge Sort Time: {time_threaded:.4f} seconds")