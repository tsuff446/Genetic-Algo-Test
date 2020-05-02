# Genetic-Algo-Test
Uses a genetic algorithm to turn a random string into a desired evolutionary target

## Requirements
1. Requires Python 3.x.x
2. Requires matplotlib

## Setup
* Set the variable "targetGenome" to be the string you want to evolve to
* mutate_chance, pop_size, max_gens, breed_num, and child_num are self-explanatory

## Examples
With targetGenome = "It was the best of times, it was the blurst of times."

Plots and a full generation log can be displayed after execution

## Algorithm
This program uses a genetic algorithm:
1. Initially, a population of strings is created, with all random allowed characters and of size near the target.
2. The population is sorted by fitness, which is based on how close the strings are to the target
3. The subset with the highest fitness is allowed to randomly "breed" with each other, mixing their characters with a chance for mutation
4. The subset with the lowest fitness are all "killed" and overwritten
5. Steps 2-4 are repeated until the target string is reached
