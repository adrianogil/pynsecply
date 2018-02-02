import os

reverse_file='invertido.txt'

with open(reverse_file, 'r') as f:
    words = f.readlines()

for w in words:
    new_s = ''
    for s in w:
        if not s.isdigit():
            new_s = new_s + s
        else:
            new_s = new_s + ' '
    new_s = new_s.strip()
    s = new_s[3:len(new_s)-1]
    print(s[::-1])

