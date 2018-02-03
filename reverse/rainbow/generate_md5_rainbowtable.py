import sys
import hashlib

target_file=sys.argv[1]
output_file=sys.argv[2]

print('Generating rainbow table from %s to %s' % (target_file, output_file))

with open(target_file, 'r') as f:
    words = f.readlines()

rainbow_words = []

for w in words:
    rainbow_words.append(hashlib.md5(w[:len(w)-1]).hexdigest() + '\n')

with open(output_file, 'w') as f:
    for w in rainbow_words:
        f.write(w)