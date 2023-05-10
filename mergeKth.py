import numpy as np
import time

def mergeKth(arr, k):
    if k > 0 and k <= len(arr):
        arr = mergeSort(arr)
        return arr[k-1]
    else:
        return None

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = mergeSort(arr[mid:])
        right = mergeSort(arr[:mid])
        return merge(left, right)
    else:
        return arr

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i < len(left):
        result += left[i:]
    elif j < len(right):
        result += right[j:]
    
    return result

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
    kthSmallest = mergeKth(arr.tolist(), k)
    end = time.perf_counter()
    print("Element Found: ", kthSmallest)
    print("Executed in ", (end-start) * 10**6, "μs")
    
if __name__ == "__main__":
    main()