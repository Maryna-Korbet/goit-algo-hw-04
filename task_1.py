import timeit
import random

#TODO: Merge sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    #Combine the smaller elements first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # If there are elements left in the left or right half, add them to the result
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result

#TODO: Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#TODO: Generate random lists of different sizes

sizes = [100, 1000, 5000, 10000]
results = {}

for size in sizes:
    arr = [random.randint(0, 100000) for _ in range(size)]
    
    merge_time = timeit.timeit(lambda: merge_sort(arr[:]), number=1)
    insertion_time = timeit.timeit(lambda: insertion_sort(arr[:]), number=1)
    timsort_time = timeit.timeit(lambda: sorted(arr[:]), number=1)
    
    results[size] = {
        "Merge Sort": merge_time,
        "Insertion Sort": insertion_time,
        "Timsort (Python's sorted)": timsort_time
    }

#TODO: Print results

for size, timings in results.items():
    print(f"Array Size: {size}")
    for algo, time_taken in timings.items():
        print(f"  {algo}: {time_taken:.6f} seconds")
    print()

