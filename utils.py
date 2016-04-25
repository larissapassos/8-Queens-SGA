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
    for i in xrange(pop_size):
        random.shuffle(base_board)
        population.append(list(base_board))

#Testing
# population = []
# generate_population(5, population)

# print "#### Population Generated ####"
# for board in population:
#   print board

# print"\n\n\n"

# bit_population = []
# encode(population, bit_population)

# print "#### Bit Population Generated ####"
# for bit_board in bit_population:
#   print bit_board

# print"\n\n\n"

# orig_population = []
# decode(bit_population, orig_population)

# print "#### Decoded Population Generated ####"
# for orig_board in orig_population:
#   print orig_board

# print"\n\n\n"