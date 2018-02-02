import os

# Using https://github.com/hulkfoo/leet

import subprocess

reverse_file='invertido.txt'

with open(reverse_file, 'r') as f:
    words = f.readlines()

# print(str(len(words[0])))

for w in words:
    # print(w[3:len(w)-1])
    cmd = "leet -u '" + w[3:len(w)-1] + "'"
    output = subprocess.check_output(cmd, shell=True)
    output = output.strip()
    print(output)