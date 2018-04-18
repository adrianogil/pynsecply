
reverse_file='invertido.txt'
with open(reverse_file, 'r') as f:
    words = f.readlines()

def analyzeChars(chars):
    char_dict = {}
    unique_chars = []

    for w in chars:
        w = w[3:len(w)-1]
        for s in w:
            if s in char_dict:
                char_dict[s] = char_dict[s] + 1
            else:
                unique_chars.append(s)
                char_dict[s] = 1

    unique_chars.sort()

    print('Unique chars: ' + str(unique_chars))

    for k in char_dict:
        print('For char "' + k + '" got ' + str(char_dict[k]) + ' references')

def analyzeCharsFromHexInvertedLines(chars):
    hex_inverted_lines = []
    for w in chars:
        w = w[3:len(w)-1][::-1].decode('hex')
        hex_inverted_lines.append(w)

    analyzeChars(hex_inverted_lines)

# analyzeChars(words)
analyzeCharsFromHexInvertedLines(words)
