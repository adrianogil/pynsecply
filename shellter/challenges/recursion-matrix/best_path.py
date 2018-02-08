# Challenge from
# https://shellterlabs.com/pt/questions/christmas-challenge-2017/recursion-matrix/
import sys

matrix_file = sys.argv[1]

with open(matrix_file, 'r') as f:
    matrix_lines = f.readlines()

matrix = []

size_x = 0
size_y = 0

for l in matrix_lines:
    m_line = l.strip().split(' ')
    size_x = len(m_line)
    matrix.append(m_line)
    size_y = size_y + 1

def find_best_path():
