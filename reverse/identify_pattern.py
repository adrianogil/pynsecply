import os

from nltk.metrics import distance
import Pycluster as PC

reverse_file='invertido.txt'

with open(reverse_file, 'r') as f:
    words = f.readlines()

dist = [distance.edit_distance(words[i], words[j])
        for i in range(1, len(words))
        for j in range(0, i)]

labels, error, nfound = PC.kmedoids(dist, nclusters=2)
cluster = dict()
for word, label in zip(words, labels):
    cluster.setdefault(label, []).append(word)
for label, grp in cluster.items():
    print(grp)