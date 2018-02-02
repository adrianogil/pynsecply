import os

# https://stackoverflow.com/questions/10492869/how-to-perform-leet-with-python
from utilitybelt import change_charset

origspace = "abcdefghijklmnopqrstuvwxyz"
keyspace  = "abcd3fgh1jklmnopqr57uvwxyz"

# print(change_charset("leetspeak",origspace, keyspace))

reverse_file='invertido.txt'

with open(reverse_file, 'r') as f:
    words = f.readlines()

for w in words:
    print(change_charset(w.lower(), keyspace, origspace))