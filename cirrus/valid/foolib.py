#!/usr/bin/env python
"""
Demo module for Cirrus Logic class

Blah blah blahdy-blah
"""

STUDENT = "Sandy"

def main():
    """
    program entry point

    :return: None
    """
    print("{} says".format(STUDENT), end=' ')
    spam()

def spam():
    """
    Some fatty canned meat stuff

    :return: None
    """

    print("hi from spam()")

def ham():
    """
    Delicious leg of the pig

    :return: None
    """
    _toast()
    print("hi from ham()")

def _toast(): # "private"
    """
    Grilled bread

    :return: None
    """
    print("TOAST TOAST")

if __name__ == '__main__':  # if run as script
    main()
