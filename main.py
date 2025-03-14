from bloom_filter import benchmark
import pandas as pd

n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
bloom_results, list_results, dict_results = benchmark(n_values, p=0.01)

bloom_df = pd.DataFrame(bloom_results)
list_df = pd.DataFrame(list_results)
dict_df = pd.DataFrame(dict_results)

print(bloom_df)
print(list_df)
print(dict_df)
