#!/usr/bin/env python

import sys

if len(sys.argv[1]) > 1:
    celsius = float(sys.argv[1])

    fahrenheit = ((9 * celsius) / 5) + 32

    print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))
else:
    print("Please provide a number on the command line")
