import os

reverse_file='invertido.txt'

with open(reverse_file, 'r') as f:
    words = f.readlines()

for w in words:
    s = w[3:len(w)-1]
    print(s[::-1])

