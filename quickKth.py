import numpy as np
import time

def quickKth(arr, k):
    if k > 0 and k <= len(arr):
        left = 0
        right = len(arr)-1
        pivotIndex = None
        while pivotIndex != k-1:
            pivotIndex, arr = partition(arr, left, right)
            if pivotIndex < k-1:
                left = pivotIndex+1
            elif pivotIndex > k-1:
                right = pivotIndex-1
        return arr[pivotIndex]
    else:
        return None

def partition(arr, left, right):
    pivot = arr[right]
    i = left-1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1, arr

def main():
    manual = input("Use custom array? (y/n) ")
    if (manual == "y"):
        print("Enter array entries (left to right, separated by space): ")
        entries = list(map(int, input().split()))
        arr = np.array(entries)
        k = int(input("Enter value k for kth smallest value to look for: "))
    else:
        n = int(input("Enter array length: "))
        arr = np.random.randint(0, 100, n)
        k = int(input("Enter value k for kth smallest value to look for: "))
    
    print("Array: ", arr)
    start = time.perf_counter()
    kthSmallest = quickKth(arr.tolist(), k)
    end = time.perf_counter()
    print("Element Found: ", kthSmallest)
    print("Executed in ", (end-start) * 10**6, "μs")
    
if __name__ == "__main__":
    main()