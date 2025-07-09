# Bubble Sort
def bubble_sort_trace(array):
    states = [array.copy()]  # Save initial state
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                states.append(array.copy())  # Save state after the swap

    return states

# Merge Sort
def merge_sort_trace(array):
    states = [array.copy()]

    def merge_sort(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid + 1, right)
            merge(arr, left, mid, right)

    def merge(arr, left, mid, right):
        L = arr[left:mid+1]
        R = arr[mid+1:right+1]
        i = j = 0
        k = left

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            states.append(arr.copy())
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            states.append(arr.copy())

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            states.append(arr.copy())

    arr_copy = array.copy()
    merge_sort(arr_copy, 0, len(arr_copy) - 1)
    return states

# Quick Sort
def quick_sort_trace(array):
    states = [array.copy()]

    def quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort(arr, low, pi - 1)
            quick_sort(arr, pi + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                states.append(arr.copy())
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        states.append(arr.copy())
        return i + 1

    arr_copy = array.copy()
    quick_sort(arr_copy, 0, len(arr_copy) - 1)
    return states