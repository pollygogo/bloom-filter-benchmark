import mmh3
import math
import timeit
import pandas as pd
import random
from bitarray import bitarray
from pympler import asizeof

def hash_int(x, m, k):
    res = []
    for i in range(k):
        res.append(mmh3.hash(str(x), seed=i) % m)
    return res

def compute_k(m, n):
    return max(1, round((m / n) * math.log(2)))

def compute_m(n, p=0.01):
    m = -(n * math.log(p)) / (math.log(2) ** 2)
    return int(m)

def create_bit_array(m):
    return bitarray(m)

def bloom_insert(n, m, k, array):
    for i in range(n):
        for j in range(k):
            h = (mmh3.hash(str(i), seed=j) % m)
            array[h] = 1

def bloom_lookup(array, val, m, k):
    for i in range(k):
        h = (mmh3.hash(str(val), seed=i) % m)
        if array[h] == 0:
            return False
    return True

def list_insert(n):
    return [i for i in range(n)]

def dict_insert(n):
    return {i: i for i in range(n)}

def benchmark(n_values, p=0.05):
    bloom_results = {'n': [], 'bloom_insert_time': [], 'bloom_lookup_present': [], 'bloom_lookup_absent': [], 'bloom_memory': []}
    list_results = {'n': [], 'list_insert_time': [], 'list_lookup_present': [], 'list_lookup_absent': [], 'list_memory': []}
    dict_results = {'n': [], 'dict_insert_time': [], 'dict_lookup_present': [], 'dict_lookup_absent': [], 'dict_memory': []}

    for n in n_values:
        m = compute_m(n, p)
        k = compute_k(m, n)
        bloom_filter = create_bit_array(m)
        
        bloom_insert_time = timeit.timeit(lambda: bloom_insert(n, m, k, bloom_filter), number=1)
        list_insert_time = timeit.timeit(lambda: list_insert(n), number=1)
        dict_insert_time = timeit.timeit(lambda: dict_insert(n), number=1)

        bloom_insert(n, m, k, bloom_filter)
        array = list_insert(n)
        dictionary = dict_insert(n)

        present_val = random.randint(0, n - 1)

        bloom_lookup_time_present = timeit.timeit(lambda: bloom_lookup(bloom_filter, present_val, n, k), number=1)
        bloom_lookup_time_absent = timeit.timeit(lambda: bloom_lookup(bloom_filter, n + 1, n, k), number=1)
        list_lookup_time_present = timeit.timeit(lambda: (present_val in array), number=1)
        list_lookup_time_absent = timeit.timeit(lambda: (n + 1 in array), number=1)
        dict_lookup_time_present = timeit.timeit(lambda: (present_val in dictionary), number=1)
        dict_lookup_time_absent = timeit.timeit(lambda: (n + 1 in dictionary), number=1)

        bloom_results['n'].append(n)
        bloom_results['bloom_insert_time'].append(bloom_insert_time)
        bloom_results['bloom_lookup_present'].append(bloom_lookup_time_present)
        bloom_results['bloom_lookup_absent'].append(bloom_lookup_time_absent)
        bloom_results['bloom_memory'].append(asizeof.asizeof(bloom_filter))

        list_results['n'].append(n)
        list_results['list_insert_time'].append(list_insert_time)
        list_results['list_lookup_present'].append(list_lookup_time_present)
        list_results['list_lookup_absent'].append(list_lookup_time_absent)
        list_results['list_memory'].append(asizeof.asizeof(array))

        dict_results['n'].append(n)
        dict_results['dict_insert_time'].append(dict_insert_time)
        dict_results['dict_lookup_present'].append(dict_lookup_time_present)
        dict_results['dict_lookup_absent'].append(dict_lookup_time_absent)
        dict_results['dict_memory'].append(asizeof.asizeof(dictionary))

    return bloom_results, list_results, dict_results
