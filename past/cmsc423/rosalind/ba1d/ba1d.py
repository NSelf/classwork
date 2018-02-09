#!/usr/bin/env python

import re

with open("rosalind_kmp.txt", "r") as f:
    lines = f.readlines()
    pattern = "(?=(%s))" % lines[0].strip('\n')
    regex = re.compile(pattern)
    for match in regex.finditer(lines[1]):
        print "%s" % (match.start()),

