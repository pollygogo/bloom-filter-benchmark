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
git clone https://github.com/YOUR-USERNAME/bloom-filter-benchmark.git cd bloom-filter-benchmark
```
