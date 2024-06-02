# os calculos de comparações e trocas ainda não estão corretos, mas o algoritmo está funcionando
def merge_sort(arr: list):
    comparisons = [0]
    swaps = [0]

    def _merge_sort(arr: list, left: int, right: int, comparisons: list, swaps: list):
        if left < right:
            mid = (left + right) // 2
            _merge_sort(arr, left, mid, comparisons, swaps)
            _merge_sort(arr, mid + 1, right, comparisons, swaps)
            merge(arr, left, mid, right, comparisons, swaps)

    def merge(arr: list, left: int, mid: int, right: int, comparisons: list, swaps: list):
        n1 = mid - left + 1
        n2 = right - mid
        L = [0] * n1
        R = [0] * n2
        for i in range(n1):
            L[i] = arr[left + i]
        for i in range(n2):
            R[i] = arr[mid + 1 + i]
        i = 0
        j = 0
        k = left
        while i < n1 and j < n2:
            comparisons[0] += 1
            if L[i] <= R[j]:
                swaps[0] += 1
                arr[k] = L[i]
                i += 1
            else:
                swaps[0] += 1
                arr[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            swaps[0] += 1
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            swaps[0] += 1
            arr[k] = R[j]
            j += 1
            k += 1


    _merge_sort(arr, 0, len(arr) - 1, comparisons, swaps)
    return arr, comparisons[0], swaps[0]
