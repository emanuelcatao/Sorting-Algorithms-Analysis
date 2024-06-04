import os
import random
import pickle

def generate_lists(sizes, num_runs):
    lists = {"random": {}, "sorted": {}, "reversed": {}}
    for size in sizes:
        lists["random"][size] = [[random.randint(0, 1000000) for _ in range(size)] for _ in range(num_runs)]
        lists["sorted"][size] = [list(range(size)) for _ in range(num_runs)]
        lists["reversed"][size] = [list(range(size, 0, -1)) for _ in range(num_runs)]
    return lists

def save_lists(lists, path_prefix):
    # Criar diretório se não existir
    os.makedirs(os.path.dirname(path_prefix), exist_ok=True)
    
    for list_type, size_lists in lists.items():
        with open(f'{path_prefix}_{list_type}.pkl', 'wb') as f:
            pickle.dump(size_lists, f)

def load_lists(path_prefix):
    lists = {}
    for list_type in ["random", "sorted", "reversed"]:
        with open(f'{path_prefix}_{list_type}.pkl', 'rb') as f:
            lists[list_type] = pickle.load(f)
    return lists
