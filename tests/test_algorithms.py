import sys
import os
import pytest
import time
import random
import csv
from sorting_algorithms import bubble_sort, heap_sort, insertion_sort, merge_sort, quick_sort, selection_sort
from sorting_algorithms import generate_lists, save_lists, load_lists

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

algorithms = [
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort
]

sizes = [1000, 10000, 50000, 100000]
num_runs = 10 # -------------------------------------> NUMERO DE TESTES :/
list_types = ["random", "sorted", "reversed"]

@pytest.fixture(scope="module", autouse=True)
def setup_lists():
    lists = generate_lists(sizes, num_runs)
    save_lists(lists, "sorting_algorithms/lists/test_lists")
    return lists

@pytest.mark.parametrize("algorithm", algorithms)
@pytest.mark.parametrize("size", sizes)
@pytest.mark.parametrize("list_type", list_types)
def test_algorithm_performance(algorithm, size, list_type, setup_lists):
    lists = setup_lists[list_type][size]
    total_comparisons = 0
    total_swaps = 0
    total_time = 0

    with open(f'results_{algorithm.__name__}_{size}_{list_type}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Run', 'Comparisons', 'Swaps', 'Time'])

        for run in range(num_runs):
            lst = lists[run]
            start_time = time.perf_counter()
            comparisons, swaps, _ = algorithm(lst.copy())
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time

            writer.writerow([run + 1, comparisons, swaps, elapsed_time])

            total_comparisons += comparisons
            total_swaps += swaps
            total_time += elapsed_time

    avg_comparisons = total_comparisons / num_runs
    avg_swaps = total_swaps / num_runs
    avg_time = total_time / num_runs

    with open('results_summary.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([algorithm.__name__, size, list_type, avg_comparisons, avg_swaps, avg_time])

    print(f"Algorithm: {algorithm.__name__}, Size: {size}, List Type: {list_type}, Avg Comparisons: {avg_comparisons}, Avg Swaps: {avg_swaps}, Avg Time: {avg_time}")

if __name__ == "__main__":
    if not os.path.exists('results_summary.csv'):
        with open('results_summary.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Algorithm', 'Size', 'List Type', 'Avg Comparisons', 'Avg Swaps', 'Avg Time'])

    pytest.main()
