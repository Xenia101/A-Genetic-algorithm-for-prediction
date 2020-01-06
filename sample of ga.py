# Sample of GA
import matplotlib.pyplot as plt
import random
import string
import time

# Settings
pre_str = "Hello"
pre_length = len(pre_str)
n_population = 10
n_parents = 5
n_elite = 2

# Initial population setting
population = []
for x in range(n_population):
    chromosome = []
    for xi in range(pre_length):
        chromosome.append(random.choice(string.ascii_letters + string.digits))
    population.append(chromosome)

# Evolution
def fitness(population):
    f_scores = []
    for chromosome in population:
        s = 0
        for x in range(pre_length):
            if pre_str[x] == chromosome[x]: s += 1
        result = [chromosome, s]
        f_scores.append(result)
    return f_scores

# Parental selection
def select_parent(f_scores):
    parents = []
    for chromosome in sorted(f_scores, key=lambda x: x[1], reverse = True)[:n_parents]:
        parents.append(chromosome[0])
    return parents

# Breeding
def breeding(parentA, parentB):
    child = []

    parentA = parents[0]
    parentB = parents[1]

    geneA = int(random.random() * pre_length)
    geneB = int(random.random() * pre_length)

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for x in range(0, pre_length):
        if (x < startGene) or (x > endGene):
            child.append(parentA[x])
        else:
            child.append(parentB[x])
    return child

def create_children(parents_pool):
    children = []
    n_new_children = len(population) - n_elite

    for x in range(0, n_elite):
        children.append(parents_pool[x])

    for x in range(0, n_new_children):
        parentA = parents_pool[int(random.random() * len(parents_pool))]
        parentB = parents_pool[int(random.random() * len(parents_pool))]
        children.append(breeding(parentA, parentB))
    return children

# Mutation / Probability
def mutation(children_set):
    for x in range(len(children_set)):
        if random.random() > 0.1: # Probability
            continue
        else:
            mutated_position = int(random.random() * pre_length)
            mutation = random.choice(string.ascii_letters + string.digits)
            children_set[x][mutated_position] = mutation
    return children_set

# Prediction & result
fitness_tracker = []
solutions = []
generations = 0
t = time.time()

while True:
    fitness_scores = fitness(population)
    fitness_tracker.append(max([x[1] for x in fitness_scores]))
    solutions.append(''.join([x[0] for x in fitness_scores if x[1] == max([x[1] for x in fitness_scores])][0]))
    print(''.join([x[0] for x in fitness_scores if x[1] == max([x[1] for x in fitness_scores])][0]))
    if max([x[1] for x in fitness_scores]) == pre_length:
        print("Generations : {0}".format(generations))
        print("{0:.2f} seconds".format(time.time() - t))
        break
    parents = select_parent(fitness_scores)
    children = create_children(parents)
    population = mutation(children)
    generations += 1

# Graph
plt.plot(list(range(generations+1)), fitness_tracker)
plt.title('Fitness Score by Generation', fontsize=14, fontweight='bold')
plt.xlabel('Generation')
plt.ylabel('Fitness Score')
plt.show()
