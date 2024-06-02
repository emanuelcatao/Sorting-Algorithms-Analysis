import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sorting_algorithms import merge_sort

def test_algorithm():
    arr = [12, 11, 13, 5, 6, 7]
    print(merge_sort(arr))

test_algorithm()