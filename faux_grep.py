#!/usr/bin/env python
import fileinput
import argparse

parser = argparse.ArgumentParser(description="Faux Grep utility")

parser.add_argument("-i", dest="ignore_case", help="ignore case",
                    action="store_true")
parser.add_argument("-n", dest="show_name", help="show file name",
                    action="store_true")
parser.add_argument("target", help="string to find")
parser.add_argument("files", nargs="+", help="files to search")

args = parser.parse_args()

target = args.target
if args.ignore_case:
    target = target.lower()

for raw_line in fileinput.input(args.files):
    if args.ignore_case:
        line_to_search = raw_line.lower()
    else:
        line_to_search = raw_line

    if target in line_to_search:
        if args.show_name:
            print(fileinput.filename(), end=' ')
        print(raw_line.rstrip())


