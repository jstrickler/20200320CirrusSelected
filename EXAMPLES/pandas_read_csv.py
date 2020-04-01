#!/usr/bin/env python
import pandas as pd
from printheader import print_header

# data from
# http://www.rita.dot.gov/bts/sites/rita.dot.gov.bts/files/publications/
# national_transportation_statistics/html/table_01_44.html

airports_df = pd.read_csv('../DATA/airport_boardings.csv', thousands=',', index_col=1)  # <1>

print_header("HEAD OF DATAFRAME")

print(airports_df.head(10), "\n")

print(airports_df['ATL':'ATL'], '\n')


print_header("SELECTED COLUMNS WITH FILTERED ROWS")
columns_wanted = ['2001 Total', 'Airport']
sort_col = '2001 Total'
max_val = 20_000_000
selector = airports_df['2001 Total'] > max_val
selected = airports_df[selector][columns_wanted]
print(selected)

print_header("COLUMN TOTALS")
print(airports_df[['2001 Total', '2010 Total']].sum(), "\n")

# print_header("'CODE' COLUMN SET AS INDEX")
# airports_df.set_index('Code')
# print(airports_df)

print_header("FIRST FIVE ROWS")
print(airports_df.iloc[:5])

# select rows through PHX where column name contains "Rank"
df1 = airports_df.loc[:'PHX',(col for col in airports_df.columns if 'Rank' in col)]
print(df1)

# select rows where row index starts with 'A'
df2 = airports_df.loc[(row for row in airports_df.index if row.startswith('A'))]
print(df2)

#  df.loc[row-selection, col-selection]
#  row-selection:   "row"  ["row1", "row2", ...]   "row1":"rowN"
print(airports_df.loc[['ATL', 'ORD', 'PHX', 'IND']])

