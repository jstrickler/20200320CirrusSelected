#!/usr/bin/env python
from glob import glob
import shlex

file_list = glob('DATA/*.csv')
print(file_list)

file_list = glob('DATA/*.wombat')
print(file_list)

muppets = 'Kermit "Miss Piggy" "Fozzy Bear" Elmo Grover'
print(muppets.split())
print(shlex.split(muppets))

