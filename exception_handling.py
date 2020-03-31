#!/usr/bin/env python
from errorlib import ValidationError

file_name = "DATA/wombats.txt"

try:
    with open(file_name) as file_in:
        pass
except FileNotFoundError as err:
    print(err)
except Exception as err:
    print(err)


data = [5, 8, 99]

try:
    print(data[12])
except IndexError as err:
    print(err)


values = 9.7, 8.1, 0.5, 0.0, 4.2, 'abc', 5.3

for v in values:
    try:
        result = 29 / v
        # print(values[97])
    except (ZeroDivisionError,TypeError) as err:
        print(err)
        break
    else:
        print(result)
    finally:
        print("Cleaning up...", v)



def doit():
    print("Hello!")
    raise ValidationError("This is a test")

try:
    doit()
except ValidationError as err:
    print(err.args[0])
    print("other values:", err.args[1:])

