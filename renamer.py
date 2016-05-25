import sys
import os
import re


if len(sys.argv) < 3:
    raise TypeError("Renamer expects at least 3 arguments.")

path = sys.argv[1]
name_to_replace = sys.argv[2]
docstring_to_replace = sys.argv[3]

if not os.path.isfile(path):
    raise OSError("Specified file does not exist.")
if name_to_replace == "":
    raise ValueError("Search string cannot be empty.")

with open(path, 'r') as f:
    file_text = f.readlines()

name_regex = name_to_replace + "\d{3,3}"
docstring_regex = docstring_to_replace + "\d{3,3}"
order = 1
new_file = []

for line in file_text:
    if re.search(name_regex, line):
        replacement = name_to_replace + str(order).zfill(3)
        line = re.sub(name_regex, replacement, line)
        order += 1
    if re.search(docstring_regex, line):
        replacement = docstring_to_replace + str(order - 1).zfill(3)
        line = re.sub(docstring_regex, replacement, line)
    new_file.append(line)

with open('renamer_output.txt', 'w') as f:
    for line in new_file:
        f.write(line)
