def quick_sort(arr):
    comparisons = [0]
    swaps = [0]

    def _quick_sort(items, low, high):
        if low < high:
            pi = partition(items, low, high)
            _quick_sort(items, low, pi - 1)
            _quick_sort(items, pi + 1, high)

    def partition(items, low, high):
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if items[j] < pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                swaps[0] += 1
        items[i + 1], items[high] = items[high], items[i + 1]
        swaps[0] += 1
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
    return comparisons[0], swaps[0], arr