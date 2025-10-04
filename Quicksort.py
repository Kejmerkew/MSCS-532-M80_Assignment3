import random
import time
import copy
import sys
sys.setrecursionlimit(10000)

# ----------------------------
# Randomized Quicksort
# ----------------------------
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)
    return arr

# ----------------------------
# Deterministic Quicksort
# ----------------------------
def deterministic_partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

def deterministic_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)
    return arr

# ----------------------------
# Benchmark Function
# ----------------------------
def benchmark_sorting_algorithms(sizes):
    results = []
    for n in sizes:
        print(f"\n=== Dataset Size: {n} ===")
        
        # Generate datasets
        datasets = {
            "Random": [random.randint(0, 10000) for _ in range(n)],
            "Sorted": list(range(n)),
            "Reverse": list(range(n, 0, -1)),
            "Repeated": [5] * n
        }
        
        for dtype, data in datasets.items():
            # Randomized Quicksort
            data_copy = copy.deepcopy(data)
            start = time.perf_counter()
            randomized_quicksort(data_copy)
            rand_time = time.perf_counter() - start
            
            # Deterministic Quicksort
            data_copy = copy.deepcopy(data)
            start = time.perf_counter()
            deterministic_quicksort(data_copy)
            det_time = time.perf_counter() - start
            
            results.append((n, dtype, rand_time, det_time))
            
            print(f"{dtype} Data:")
            print(f"  Randomized Quicksort: {rand_time:.6f} s")
            print(f"  Deterministic Quicksort: {det_time:.6f} s")
    return results

# ----------------------------
# Run Benchmark
# ----------------------------
if __name__ == "__main__":
    sizes = [1000, 2000, 5000]
    results = benchmark_sorting_algorithms(sizes)
