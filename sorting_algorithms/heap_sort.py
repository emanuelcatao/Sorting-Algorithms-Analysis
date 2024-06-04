'''
Heap Sort
Best: O(n log n)
Average: O(n log n)
Worst: O(n log n)

Space Complexity: O(1)
Stable: No

Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure.
It is similar to selection sort where we first find the maximum element and place
the maximum element at the end. We repeat the same process for the remaining elements.

The heap sort algorithm involves preparing the list by first turning it into a max heap.
The algorithm then repeatedly swaps the first value of the list with the last value,
decreases the range of values considered in the heap operation, and finally heapify the
new heap. The heapify function can be performed in O(log n) time.
'''
def heap_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n // 2 - 1, -1, -1): # Aqui construimos o max heap
        comparisons, swaps = heapify(arr, n, i, comparisons, swaps)
    for i in range(n-1, 0, -1): # aplicamos o heap sort em si
        arr[i], arr[0] = arr[0], arr[i]
        swaps += 1
        comparisons, swaps = heapify(arr, i, 0, comparisons, swaps) # heapify o heap reduzido, para manter a propriedade de max heap
    return comparisons, swaps, arr

def heapify(arr, n, i, comparisons, swaps):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n:
        comparisons += 1
        if arr[left] > arr[largest]:
            largest = left
    if right < n:
        comparisons += 1
        if arr[right] > arr[largest]:
            largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        swaps += 1
        comparisons, swaps = heapify(arr, n, largest, comparisons, swaps)
    return comparisons, swaps