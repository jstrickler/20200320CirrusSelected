#!/usr/bin/env python
import numpy as np
import pandas as pd
from printheader import print_header  # <1>

dataset1 = np.arange(9.).reshape((3, 3))  # <2>

df1 = pd.DataFrame(  # <3>
    dataset1,
    columns=['apple', 'banana', 'mango'],
    index=['orange', 'purple', 'blue']
)

dataset2 = np.arange(12.).reshape((4, 3))  # <2>

df2 = pd.DataFrame(  # <3>
    dataset2,
    columns=['apple', 'banana', 'kiwi'],
    index=['orange', 'purple', 'blue', 'brown']
)

print_header('df1')
print(df1)  # <4>
print()

print_header('df2')
print(df2)  # <4>
print()

print_header('df1 + df2')
print(df1 + df2)  # <5>

print_header('df1.add(df2, fill_value=0)')
print(df1.add(df2, fill_value=0))  # <6>
print('-' * 60)
df3 = df1 + df2

print(df3)
df3[np.isnan(df3)] = -1
print(df3)

print(df1.columns, '\n')
print(df1.shape, '\n')
print(df1.head(2), '\n')
print(df1.tail(2), '\n')
print(df1.values, '\n')

print(df1.info(memory_usage="deep"), '\n')

print(df1.describe())

df1.to_csv("junk.csv")
