reverse_file='invertido.txt'

# By analyzing file, I found it starts with 7000 and finishes with 9000
# > cat ../invertido.txt | cut -c4- | rev | head -1 | xa python rainbow_table.py {}
#    Testing string: 708be71b9ab6e0a84252760579ade9f1
#    Found: 7000
# > cat ../invertido.txt | cut -c4- | rev | tail -1 | xa python rainbow_table.py {}
#    Testing string: d5ab8dc7ef67ca92e41d730982c5c602
#    Found: 9000

import hashlib



with open(reverse_file, 'r') as f:
    words = f.readlines()

for i in xrange(0, len(words)):
    w = words[i]
    w = w[3:len(w)-1][::-1]
    if w != hashlib.md5(str(7000+i)).hexdigest():
        print('Found different line:\n'+w)