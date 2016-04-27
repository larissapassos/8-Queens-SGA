import random
from random import random as roll
import utils
from operator import itemgetter

class SGA:
    def __init__(self):
        self.crossover_prob = 1.0
        self.mutation_prob = 0.8
        self.iteration_limit = 10000
        self.pop_fit_pairs = []

    def fitness_board(self, board):
        conflicts = 0
        orig_board = utils.decode_board(board)
        for i in range(utils.num_queens):
            for j in range(i + 1, utils.num_queens):
                if utils.diagonal(orig_board, i, j):
                    # same diagonal
                    conflicts += 1
                elif orig_board[i] == orig_board[j]:
                    # same column
                    conflicts += 1
        fitness = float(1) / (1 + conflicts)
        return fitness

    def calculate_fitness(self, population, child_1, child_2):
        if child_1 is None and child_2 is None:
            for board in population:
                fit = self.fitness_board(board)
                utils.insert_in_order(self.pop_fit_pairs, board, fit)
        else:
            fitness_1 = self.fitness_board(child_1)
            fitness_2 = self.fitness_board(child_2)
            utils.insert_in_order(self.pop_fit_pairs, child_1, fitness_1)
            utils.insert_in_order(self.pop_fit_pairs, child_2, fitness_2)
        return self.pop_fit_pairs[0]

    def trim_population(self):
        self.pop_fit_pairs.pop()
        self.pop_fit_pairs.pop()

    def tournament(self):
        candidates = random.sample(self.pop_fit_pairs, 5)
        sorted_candidates = sorted(candidates, key=itemgetter(1), reverse=True)
        return sorted_candidates[0][0], sorted_candidates[1][0]

    # def roulette():

    def has_column(self, partial_board, column):
        for i in range(0, len(partial_board), utils.bit_num_size):
            board_column = partial_board[i : i + utils.bit_num_size]
            if board_column == column:
                return True
        return False

    def crossover(self, parent_1, parent_2, verbose=0):
        crossover_point = random.randint(1, utils.num_queens - 1)
        if verbose==2:
            print "crossover_point: ", crossover_point
        crossover_bit = crossover_point * utils.bit_num_size

        child_1 = parent_1[: crossover_bit]
        child_2 = parent_2[: crossover_bit]

        for i in range(crossover_bit, utils.bit_board_size + crossover_bit, utils.bit_num_size):
            index = i % utils.bit_board_size
            next_bit_1 = parent_1[index : index + utils.bit_num_size]
            next_bit_2 = parent_2[index : index + utils.bit_num_size]

            if not self.has_column(child_2, next_bit_1):
                child_2 += next_bit_1
            if not self.has_column(child_1, next_bit_2):
                child_1 += next_bit_2

        return child_1, child_2

    def mutation(self, board):
        chance = roll()
        if chance >= self.mutation_prob:
            return board
            # applyMutation()
        return board

    def sga(self, population_size, parent_selection=None,
            n_steps=10000, verbose=0):
        if parent_selection is None:
            parent_selection = self.tournament
        population = []
        # self.pop_fit_pairs = []
        utils.generate_population(population_size, population)
        # print population
        steps = 0
        max_fitness = -1
        max_ind = ""
        avg_fitness_lst = []
        max_fitness_lst = []

        child_1 = None
        child_2 = None

        while max_fitness < 1 and steps < n_steps:
            # Add childs in population and calculate their fitness
            max_ind, max_fitness = self.calculate_fitness(population, child_1, child_2)

            if (child_1 is not None and child_2 is not None):
                # Remove the 2 worst individuals from population
                if verbose==2:
                    print "Trimming population"
                self.trim_population()

            avg_fitness = utils.avg(self.pop_fit_pairs)
            max_fitness_lst.append(max_fitness)
            avg_fitness_lst.append(avg_fitness)
            if verbose == 1:
                print "max_fitness=%.6f" % max_fitness
                print "avg_fitness=%.6f" % avg_fitness
            if (max_fitness == 1.0):
                #solution
                if verbose == 1:
                    print "Solution found"
                break

            # Crossover and mutation
            parent_1, parent_2 = parent_selection()
            if verbose == 2:
                print "parents: ", parent_1, parent_2
            child_1, child_2 = self.crossover(parent_1, parent_2, verbose)
            if verbose == 2:
                print "childs: ", child_1, child_2
            self.mutation(child_1)
            self.mutation(child_2)

            steps += 1
            if verbose == 1:
                print "steps: {0}".format(steps)

        # Populate solution
        solution = {"max_fitness": max_fitness, "avg_fitness": avg_fitness,
            "individual": utils.decode_board(max_ind), "avg_fitness_lst": avg_fitness_lst,
            "max_fitness_lst": max_fitness_lst, "steps": steps}
        if verbose==2:
            print "solution: ", solution
        return solution
