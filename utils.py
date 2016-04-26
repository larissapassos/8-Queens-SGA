import random

bit_num_size = 3
num_queens = 8
bit_board_size = bit_num_size * num_queens

base_board = range(num_queens)

def encode_number(number):
    bit_number = bin(number)[2 :].zfill(bit_num_size)
    return bit_number

def decode_number(bit_number):
    number = int(bit_number, 2)
    return number

def encode_board(board):
    bit_board = []
    for column in board:
        bit_board.append(encode_number(column))
    return "".join(bit_board)

def decode_board(bit_board):
    board = []
    for i in range(0, bit_board_size, bit_num_size):
        board.append(decode_number(bit_board[i : i + bit_num_size]))
    return board

def encode(population, bit_population):
    for board in population:
        bit_population.append(encode_board(board))

def decode(bit_population, population):
    for bit_board in bit_population:
        population.append(decode_board(bit_board))

def generate_population(pop_size, population):
    pop = []
    for i in xrange(pop_size):
        random.shuffle(base_board)
        pop.append(list(base_board))
    encode(pop, population)

def diagonal(board, i, j):
    if abs(j - i) == abs(board[j] - board[i]):
        return True
    return False

def insert_in_order(lst_pairs, board, fitness):
    # Binary search and insertion to keep the pairs ordered so we can trim them easily
    lo = 0
    hi = len(lst_pairs)
    while lo < hi:
        mid = (lo + hi) / 2
        if lst_pairs[mid][1] > fitness:
            lo = mid + 1
        else:
            hi = mid
    lst_pairs.insert(lo, (board, fitness))

def avg(lst_pairs):
    sum = 0
    for gene, fitness in lst_pairs:
        sum += fitness
    return sum / float(len(lst_pairs))