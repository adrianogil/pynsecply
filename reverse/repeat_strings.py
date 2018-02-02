import os

def get_patterns():
    reverse_file='invertido.txt'

    with open(reverse_file, 'r') as f:
        lines = f.readlines()

    words = []

    for l in lines:
        words.append(l[3:len(l)-1])

    word_size = len(words[0])

    min_pttrn = 3
    max_pttrn = word_size - 4

    pttrn = {}

    for w in words:
        for ps in xrange(min_pttrn, max_pttrn):
            for i in xrange(0, word_size - ps):
                candidate_pttrn = w[i:(i+ps)]
                number_repeat = 0
                if not candidate_pttrn in pttrn:
                    for wp in words:
                        for i in xrange(0, word_size - ps):
                            if wp[i:(i+ps)] == candidate_pttrn:
                                number_repeat = number_repeat + 1
                    if number_repeat > 1:
                        pttrn[candidate_pttrn] = number_repeat
                        print('pattern "' + candidate_pttrn + '" was repeated ' + str(number_repeat))
