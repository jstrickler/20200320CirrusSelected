#!/usr/bin/env python
from exception_handling import doit
from errorlib import ValidationError

try:
    doit()
except ValidationError as err:
    print(err)

