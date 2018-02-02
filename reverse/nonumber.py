import os

reverse_file='invertido.txt'

with open(reverse_file, 'r') as f:
    words = f.readlines()

for w in words:
    new_s = ''
    for s in w:
        if not s.isdigit():
            new_s = new_s + s
    new_s = new_s.strip()
    print(new_s)

