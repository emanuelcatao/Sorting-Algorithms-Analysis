'''
Merge Sort

Best: O(n log n)
Average: O(n log n)
Worst: O(n log n)

Space Complexity: O(n)
Stable: Yes

Merge Sort is a divide and conquer algorithm that divides the input list into two halves,
recursively sorts the two halves, and then merges the sorted halves. The merge() function
is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that
arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
'''
# os calculos de comparações e trocas ainda não estão corretos, mas o algoritmo está funcionando
def merge_sort(arr: list):
    comparisons = [0]
    swaps = [0]

    # Aqui é o merge sort de fato, o merge_sort é apenas um wrapper e não é chamado recursivamente
    # o merge é chamado para ordenar e unir as listas de maneira ordenada
    def _merge_sort(arr: list, left: int, right: int, comparisons: list, swaps: list):
        if left < right:
            mid = (left + right) // 2
            _merge_sort(arr, left, mid, comparisons, swaps)
            _merge_sort(arr, mid + 1, right, comparisons, swaps)
            merge(arr, left, mid, right, comparisons, swaps)

    def merge(arr: list, left: int, mid: int, right: int, comparisons: list, swaps: list):
        #print(arr)
        #print(f"left={left} mid={mid} right={right}")
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
            #print(L, R)
            comparisons[0] += 1
            #print(f"L[{i}]={L[i]}", f"-  R[{j}]={R[j]}")
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
            #print(f"L[{i}]={L[i]}")
            swaps[0] += 1
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            #print(f"R[{j}]={R[j]}")
            swaps[0] += 1
            arr[k] = R[j]
            j += 1
            k += 1


    _merge_sort(arr, 0, len(arr) - 1, comparisons, swaps)
    return comparisons[0], swaps[0], arr
