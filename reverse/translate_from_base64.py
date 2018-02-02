import base64,os

reverse_file='invertido.txt'

with open(reverse_file, 'r') as f:
    words = f.readlines()

print(str(len(words[0])))

for w in words:
    # print(w[3:len(w)-1])
    print(base64.b64decode(w[3:len(w)-1]))