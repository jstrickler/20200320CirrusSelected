#!/usr/bin/env python
import csv

with open('../DATA/parasite_data.csv') as data_in:
    rdr = csv.reader(data_in)  # <1>
    header = next(rdr) # read first row
    for row in rdr:  # <2>
        print(row)

print('-' * 60)

with open('../DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    for row in rdr:
        print(row)

