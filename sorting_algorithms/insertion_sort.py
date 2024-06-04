def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        if arr[j] <= key:
            comparisons += 1
            continue
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
        arr[j + 1] = key
        if j >= 0:
            comparisons += 1
    return comparisons, swaps, arr
