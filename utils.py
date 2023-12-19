import numpy as np
import random 
from random import randint

def get_items():
    values = []
    weights = []
    num_items = int(input("Enter number of items: "))
    for i in range(num_items):
        value = int(input("Enter value: "))
        weight = int(input("Enter weight: "))
        values.append(value)
        weights.append(weight)
    return values, weights


def initialization(population_size, length, max_weight, weights, isUnbounded):
    if isUnbounded:
        return [[random.randint(0, max_weight // weight) for weight in weights] for _ in range(population_size)]
    else:
        return [[random.randint(0, 1) for _ in range(length)] for _ in range(population_size)]

def fitness(chromosome, values, weights, max_weight):
    total_value = np.sum(np.array(chromosome) * np.array(values))
    total_weight = np.sum(np.array(chromosome) * np.array(weights))
    if total_weight > max_weight:
        return 0  
    return total_value

def crossover(parent1, parent2):
    crossover_point = np.random.randint(0, len(parent1))
    parent1, parent2 = np.array(parent1), np.array(parent2)  # Convert lists to NumPy arrays
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

def mutate(chromosome, mutation_rate, max_weight, weights, isUnbounded):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            if isUnbounded:
                chromosome[i] = random.randint(0, max_weight // weights[i])
            else:
                chromosome[i] = 1 - chromosome[i]
    return chromosome

def genetic_algorithm(values,
                    weights,
                    max_weight,
                    population_size=100,
                    generations=100,
                    crossover_rate=0.8,
                    mutation_rate=0.01,
                    unbounded=False):
    
    population = initialization(population_size, len(values), max_weight, weights, unbounded)
    print('\n')
    print(population)
    for generation in range(generations):
        fitness_values = np.array([fitness(chromosome, values, weights, max_weight) for chromosome in population])
        sorted_indices = np.argsort(fitness_values)[::-1]
        sorted_indices = list(sorted_indices)  # Convert sorted_indices to a Python list
        population = [population[i] for i in sorted_indices]  # Reorder the population list
        new_population = []
        for i in range(0, population_size, 2):
            # Select two parents
            parent_indices = np.random.choice(len(population), size=2, replace=False)
            parent1, parent2 = population[parent_indices[0]], population[parent_indices[1]]
            # Perform crossover with a certain probability
            if np.random.rand() < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1.copy(), parent2.copy() 
                

            child1 = mutate(child1, mutation_rate, max_weight, weights, unbounded)
            child2 = mutate(child2, mutation_rate, max_weight, weights, unbounded)
            
            # Add the children to the new population
            new_population.append(child1)
            new_population.append(child2)

        
        # Replace the old population with the new population
        population = np.array(new_population)[:population_size]

        # Find the best solution in the final population
    best_solution = max(population, key=lambda x: fitness(x, values, weights, max_weight))
    
    print("Final Population:")
    for chromosome in population:
        print(f"Chromosome: {chromosome}, Fitness: {fitness(chromosome, values, weights, max_weight)}")
    best_value = fitness(best_solution, values, weights, max_weight)
    return best_solution , best_value
