import socket, sys

# PORT = 12345
# HOSTNAME = '54.209.5.48'

word_pt_file = '../../reverse/rainbow/words_pt.txt'
word_en_file = '../../reverse/rainbow/words_en.txt'



def verify_word_in_dictionary(word):
    with open(word_pt_file, 'r') as f:
        words_pt = f.readlines()
    with open(word_en_file, 'r') as f:
        words_en = f.readlines()

    words_l = [words_pt, words_en]

    ws_count = 0
    for ws in words_l:
        count = 0
        for w in ws:
            if w.strip() == word:
                print(count)
                return
            count = count + 1
        ws_count = ws_count + 1

def netcat_attempts_to_login(ws_start = 0, w_start = 0):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(( HOSTNAME, PORT ))
    data = s.recv(1024)
    print data

    rec_data = []
    with open(word_pt_file, 'r') as f:
        words_pt = f.readlines()
    with open(word_en_file, 'r') as f:
        words_en = f.readlines()

    words_l = [words_pt, words_en]

    ws_count = 0
    w_count = 0

    for ws in words_l:
        if ws_count < ws_start:
            ws_count = ws_count + 1
            continue
        w_count = 0
        for w in ws:
            if w_count < w_start:
                w_count = w_count + 1
                continue
            w = w[:len(w)-1]
            print('Testing (%s,%s) "%s"' % (ws_count, w_count, w) )
            s.sendall(w)
            data = s.recv(1024)
            # print data
            if not 'WRONG! Try Again!' in data:
                print('Interesting attempt got response')
                print data
                s.shutdown(socket.SHUT_WR)
                s.close()
                return
            w_count = w_count + 1
        ws_count = ws_count + 1
            # if count == 3:
            #     s.shutdown(socket.SHUT_WR)
            #     s.close()
            #     return

    # while 1:
    #     data = s.recv(1024)
    #     print data
    #     if not data:
    #         break
    #     elif count <= 20:
    #         s.sendall(text_to_send)
    #         count = count + 1
    #     rec_data.append(data)

    s.shutdown(socket.SHUT_WR)
    s.close()

    return rec_data

def netcat(text_to_send):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(( HOSTNAME, PORT ))
    s.sendall(text_to_send)

    rec_data = []
    count = 0
    while 1:
        data = s.recv(1024)
        print data
        if not data:
            break
        elif count <= 20:
            s.sendall(text_to_send)
            count = count + 1
        rec_data.append(data)

    s.shutdown(socket.SHUT_WR)
    s.close()

    return rec_data

if __name__ == '__main__':
    # text_to_send = 'password'
    # text_recved = netcat( text_to_send)
    # if text_recved:
    #     print text_recved
    netcat_attempts_to_login(int(sys.argv[1]), int(sys.argv[2]))
    # verify_word_in_dictionary(sys.argv[1])