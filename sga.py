import random
import utils

crossover_prob = 1.0
mutation_prob = 0.8
iteration_limit = 10000
num_queens = 8

pop_fit_pairs = []

def fitness_board(board):
    conflicts = 0
    orig_board = utils.decode_board(board)
    for i in range(num_queens):
        for j in range(i + 1, num_queens):
            if utils.diagonal(orig_board, i, j):
                # same diagonal
                conflicts += 1
            elif orig_board[i] == orig_board[j]:
                # same column
                conflicts += 1
    print "Number of conflicts ", conflicts
    fitness = float(1) / (1 + conflicts)
    return fitness

def calculate_fitness(population, child_1, child_2):
    if child_1 is None and child_2 is None:
        for board in population:
            fit = fitness_board(board)
            utils.insert_in_order(pop_fit_pairs, board, fit)
    else:
        fitness_1 = fitness_board(child_1)
        fitness_2 = fitness_board(child_2)
        utils.insert_in_order(pop_fit_pairs, child_1, fitness_1)
        utils.insert_in_order(pop_fit_pairs, child_2, fitness_2)
    return pop_fit_pairs[0]

def trim_population():
    pop_fit_pairs.pop()
    pop_fit_pairs.pop()

# def tournament():

# def roulette():

# def crossover(parent_1, parent_2):

# def mutation(board):

def sga(population_size, parent_selection):
    population = []
    utils.generate_population(population_size, population)
    steps = 0
    max_fitness = -1
    max_ind = ""
    avg_fitness_lst = []
    max_fitness_lst = []

    child_1 = None
    child_2 = None

    while max_fitness < 1 and steps < 10000:
        # Add childs in population and calculate their fitness
        max_ind, max_fitness = calculate_fitness(population, child_1, child_2)

        if (child_1 is not None and child_2 is not None):
            # Remove the 2 worst individuals from population
            trim_population()

        avg_fitness = utils.avg(pop_fit_pairs)
        max_fitness_lst.append(max_fitness)
        avg_fitness_lst.append(avg_fitness)

        if (max_fitness == 1.0):
            #solution
            break

        # Crossover and mutation
        parent_1, parent_2 = parent_selection()
        child_1, child_2 = crossover(parent_1, parent_2)
        mutation(child_1)
        mutation(child_2)

        steps += 1

    # Populate solution
    solution = {"max_fitness": max_fitness, "avg_fitness": avg_fitness,
        "individual": utils.decode(max_ind), "avg_fitness_lst": avg_fitness_lst,
        "max_fitness_lst": max_fitness_lst, "steps": steps}
    return solution