#!/usr/bin/env python

STUDENT = "Sandy"

def main():
    print("{} says".format(STUDENT), end=' ')
    spam()

def spam():
    print("hi from spam()")

def ham():
    _toast()
    print("hi from ham()")

def _toast(): # "private"
    print("TOAST TOAST")

if __name__ == '__main__':  # if run as script
    main()
