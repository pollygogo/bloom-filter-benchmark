# bloom-filter-benchmark

A Python project that benchmarks Bloom Filters against traditional data structures (lists and dictionaries).

## Overview

This project implements a Bloom Filter, a probabilistic data structure, and compares its efficiency with lists and dictionaries in terms of:
- Insertion time
- Lookup time (present and absent values)
- Memory usage

## Features

- Implements Bloom Filter using MurmurHash3 (`mmh3`) and `bitarray`
- Computes optimal hash function count (k) and bit array size (m)
- Benchmarks against list and dictionary for efficiency
- Measures execution time and memory footprint

## Installation

### Clone the Repository
```
git clone https://github.com/pollygogo/bloom-filter-benchmark.git
cd bloom-filter-benchmark
```

### Install Dependencies
Ensure you have Python 3.x installed. Then, install the required packages:
```
pip install -r requirements.txt
```

## Usage

Run the benchmarking script:
```
python main.py
```

This will:
- Insert values into a Bloom Filter, list, and dictionary
- Measure the time taken for insertion and lookup
- Display results in Pandas DataFrames

## Sample Output
```
n=1, m=9, k=6
n=10, m=95, k=7
n=100, m=958, k=7
n=1000, m=9585, k=7
n=10000, m=95850, k=7
n=100000, m=958505, k=7
n=1000000, m=9585058, k=7
         n  bloom_insert_time  bloom_lookup_present  bloom_lookup_absent  bloom_memory
0        1           0.000030              0.000003         1.833000e-06            88
1       10           0.000010              0.000001         1.583000e-06            96
2      100           0.000096              0.000002         9.579999e-07           200
3     1000           0.000837              0.000001         8.340003e-07          1280
4    10000           0.008511              0.000001         1.125000e-06         12064
5   100000           0.064696              0.000003         8.750003e-07        119896
6  1000000           0.648710              0.000003         9.169999e-07       1198216
         n  list_insert_time  list_lookup_present  list_lookup_absent  list_memory
0        1          0.000001         3.750001e-07        2.910001e-07          120
1       10          0.000001         3.329997e-07        2.920005e-07          504
2      100          0.000002         3.330006e-07        6.669998e-07         4120
3     1000          0.000020         2.209000e-06        4.791000e-06        40856
4    10000          0.000163         3.512500e-05        3.816600e-05       405176
5   100000          0.001425         1.247500e-04        3.329580e-04      4000984
6  1000000          0.019078         3.435209e-03        4.258125e-03     40448728
         n  dict_insert_time  dict_lookup_present  dict_lookup_absent  dict_memory
0        1      7.079998e-07         2.079996e-07        2.919996e-07          256
1       10      9.590003e-07         2.500001e-07        2.500001e-07          672
2      100      3.167000e-06         2.079996e-07        1.250000e-07         7888
3     1000      2.633300e-05         1.660001e-07        1.250000e-07        68952
4    10000      2.505000e-04         2.079996e-07        2.079996e-07       614992
5   100000      3.125917e-03         3.330006e-07        3.750001e-07      8442960
6  1000000      3.312212e-02         1.957999e-06        2.910001e-07     73943128
```

## How It Works

1. **Optimal Bloom Filter Parameters**
   - `compute_m(n, p)`: Computes the bit array size (`m`) based on `n` (number of elements) and `p` (false positive probability).
   - `compute_k(m, n)`: Computes the number of hash functions (`k`) for optimal performance.

2. **Bloom Filter Operations**
   - `bloom_insert(n, m, k, array)`: Inserts elements into the Bloom Filter.
   - `bloom_lookup(array, val, m, k)`: Checks if an element is likely present.

3. **Benchmarking**
   - Inserts and searches for elements in Bloom Filter, List, and Dictionary.
   - Compares execution time and memory usage.
     
## Notes

- Bloom Filters cannot store elements directly but indicate membership probabilistically.
- False positives are possible, but false negatives are not.
- Suitable for applications like web caches, spell checkers, and database queries.





