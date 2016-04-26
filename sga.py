import random
import utils

crossover_prob = 1.0
mutation_prob = 0.8
iteration_limit = 10000

def tournament(population, fitness):

def crossover(parent_1, parent_2):

def mutation(board):

def fitness(board):

def survival(population, new_boards):

def sga(population_size, parent_selection):
    population = []
    utils.generate_population(population_size, population)
    steps = 1
    max_fitness = -1
    max_idx = -1
    avg_fitness_lst = []
    max_fitness_lst = []

    child_1 = None
    child_2 = None

    while max_fitness < 1 or steps <= 10000:
        fitness = []
        # Add childs in population and calculate their fitness
        max_fitness, max_idx = calculate_fitness(population, fitness, child_1, child_2)

        if (child_1 is not None and child_2 is not None):
            # Remove the 2 worst individuals from population
            trim_population(population, fitness)

        avg_fitness = avg(fitness)
        max_fitness_lst.append(max_fitness)
        avg_fitness_lst.append(avg_fitness)

        if (max_fitness == 1):
            #solution
            break

        # Crossover and mutation
        parent_1, parent_2 = parent_selection(population, fitness)
        child_1, child_2 = crossover(parent_1, parent_2)
        mutation(child_1)
        mutation(child_2)

        steps += 1

    # Populate solution
    solution = {"max_fitness": max_fitness, "individual": utils.decode(population[max_idx],
        "avg_fitness_lst": avg_fitness_lst, "max_fitness_lst": max_fitness_lst, "steps": steps)}
    return solution