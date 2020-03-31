#!/usr/bin/env python
from dataclasses import make_dataclass
import sqlite3


def dataclass_cursor(cursor):
    '''Generate rows as named tuples'''
    column_names = [desc[0] for desc in cursor.description]
    row_class = make_dataclass('row_tuple', column_names)

    for cursor_row in cursor.fetchall():
        row_instance = row_class(*cursor_row)
        yield row_instance


with sqlite3.connect("../DATA/presidents.db") as s3conn:
    c = s3conn.cursor()

    # select first name, last name from all presidents
    num_recs = c.execute('''
        select firstname, lastname
        from presidents
    ''')

    for row in dataclass_cursor(c):
        print(row.firstname, row.lastname)
