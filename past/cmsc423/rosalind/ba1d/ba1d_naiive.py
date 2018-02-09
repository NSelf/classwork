#!/usr/bin/env python

import re

with open("rosalind_kmp.txt", "r") as f:
    lines = f.readlines()
    pattern = "(?=(%s))" % lines[0].strip('\n')
    text = "".join(line.strip("\n") for line in lines) 
    regex = re.compile(pattern)
    for match in regex.finditer(text):
        print "%s" % (match.start()),

