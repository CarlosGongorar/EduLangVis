def bubble_sort_trace(array):
    """Bubble Sort that returns a list of array states after each swap."""
    states = [array.copy()]  # Save initial state
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                states.append(array.copy())  # Save state after the swap

    return states
