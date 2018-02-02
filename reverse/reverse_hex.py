import os

reverse_file='invertido.txt'

with open(reverse_file, 'r') as f:
    words = f.readlines()

min_w_size = 4

line_number = 1

# https://stackoverflow.com/questions/10492869/how-to-perform-leet-with-python
from utilitybelt import change_charset

origspace = "0123456789abcdef"
keyspace  = "fedcba9876543210"

for w in words:
    # if line_number == 389:
    #     print(w)
    #     w = w[3:len(w)-1][::-1]
    #     for i in xrange(0, len(w), 2):
    #         print(w[i:i+2] + ' - ' + w[i:i+2].decode('hex'))

    # h = change_charset(w[3:len(w)-1][::-1], origspace, keyspace).decode('hex')
    try:
        h = change_charset(w[3:len(w)-1][::-1], origspace, keyspace).decode('hex')
        # h = change_charset(w[3:len(w)-1][::-1], origspace, keyspace)
        print(h)
    except:
        continue

    continue
    line = str(line_number) + ' - '
    new_s = ''
    found_sth = False
    for s in h:
        if s.lower() in "abcdefghijklmnopqrstuvwxyz":
            new_s = new_s + s
        else:
            if len(new_s) > min_w_size:
                line = line + new_s + ' - '
                found_sth = True
            new_s = ' '
    if len(new_s) > min_w_size:
        line = line + new_s + ' - '
        found_sth = True

    if found_sth == True:
        print(line)

    line_number = line_number + 1

