# A Genetic Algorithm for prediction

유전 알고리즘을 이용한 (문자열)예측

### A Genetic Algorithm 란?
>In computer science and operations research, a genetic algorithm (GA) is a metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on bio-inspired operators such as mutation, crossover and selection.
[WIKIPEDIA](https://en.wikipedia.org/wiki/Genetic_algorithm)

## 예시 / 동작 방식

1. Variables setting

```python
pre_str = "Hello"         # 예측을 원하는 문자열
pre_length = len(pre_str) # 위 문자열의 길이
n_population = 10         # 유전자들의 수
n_parents = 5             # 부모의 수
n_elite = 2               # 돌연변이 수
```

2. Initial population setting

```python
population = [] 
for x in range(n_population):
    chromosome = []
    for xi in range(pre_length):
        chromosome.append(random.choice(string.ascii_letters + string.digits))
    population.append(chromosome)

# population
['C', '8', '6', 'e', 'E']
['1', 'P', 't', 'l', '9']
['Y', 'X', 'i', 'R', '8']
['X', 'k', 'B', 'N', 'b']
['I', '3', 'i', 'R', '7']
['O', '8', 'U', '5', 'A']
['1', 'c', 'F', 'r', 'd']
['f', 'q', 'a', 'a', 'U']
['m', 'K', '0', 'G', '3']
['E', 'W', '8', 'q', 'e']
```

3. Evolution

```python
# fitness(population)
[['w', 'V', '2', 'T', 'J'], 0]
[['f', 'a', '6', 'b', 'b'], 0]
[['F', '8', 'B', 'I', 'J'], 0]
[['E', 'I', 'a', 'x', 'h'], 0]
[['F', 'K', 'q', 'l', 'S'], 1]
[['X', 'T', '4', '2', 'F'], 0]
[['4', 'h', 'g', '7', 'h'], 0]
[['e', 'c', 'n', 'D', 'M'], 0]
[['A', 'f', 'Q', 'p', 'p'], 0]
[['S', 'K', 'T', 'h', '1'], 0]
```

4. Parental selection

```python
# select_parent(fitness(population))
['9', 'X', 'H', 'g', 'o']
['h', 'Q', 'f', '6', 'T']
['h', '8', 'h', 'm', 'T']
['a', 'z', 'S', 'c', 'T']
['t', 'E', '1', 'B', 'T']
```

5. Breeding

```python
def breeding(parentA, parentB)

def create_children(parents_pool)
```

6. 
