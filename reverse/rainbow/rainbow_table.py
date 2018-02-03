
original_tables = ['numbers.txt', 'words_pt.txt']
rainbow_tables = ['numbers_md5.txt', 'words_pt_md5.txt']

def test_all_rainbow_tables(md5_v):
    for i in xrange(0, len(original_tables)):
        result = get_value_from_rainbow_table(md5_v, original_tables[i],
                                                     rainbow_tables[i])
        if result[0]:
            return result
    return (False,)


def get_value_from_rainbow_table(md5_v,original_table,rainbow_table):
    md5_v = md5_v.strip()
    with open(original_table, 'r') as f:
        original_words = f.readlines()
    with open(rainbow_table, 'r') as f:
        rainbow_table_words = f.readlines()
    for i in xrange(0, len(rainbow_table_words)):
        rbw = rainbow_table_words[i].strip()
        if rbw == md5_v:
            return (True, original_words[i].strip())
    return (False, )

if __name__ == '__main__':
    import sys
    print('Testing string: '+sys.argv[1])
    result=test_all_rainbow_tables(sys.argv[1])
    if result[0]:
        print('Found: ' + result[1])
    else:
        print('Not found!')

    