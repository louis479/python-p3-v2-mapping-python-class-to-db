#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

d1 = Department("Engineering", "New York")
d1.save()

ipdb.set_trace()
