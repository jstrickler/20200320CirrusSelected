#!/usr/bin/env python
import electrical as elec  # <1>
import navigation as nav  # <2>

from electrical import current as ecurrent
from navigation import current as ncurrent

print(elec.current())  # <3>
print(nav.current())  # <4>

# import from....
# 1. current folder
# 2. folders in PYTHONPATH if it exists
# 3. sys.prefix/lib ...
