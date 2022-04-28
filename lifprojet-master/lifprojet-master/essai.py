import dask.dataframe as dd
import pandas as pd

print('1')
df = dd.read_json('../part-00198.json')
print('2')
print(df.head())
print('3')
print(df.tail())
print('end')