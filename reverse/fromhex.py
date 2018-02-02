import os

reverse_file='invertido.txt'

with open(reverse_file, 'r') as f:
    words = f.readlines()

for w in words:
    # print(w[3:len(w)-1].decode('hex'))
    print(w[3:len(w)-1])

