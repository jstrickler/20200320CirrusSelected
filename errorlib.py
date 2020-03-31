#!/usr/bin/env python

class ValidationError(Exception):
    def __init__(self, *args):
        if args == ():
            self.args = ("Your data is corrupt",)
    pass
