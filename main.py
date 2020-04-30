import random
import matplotlib.pyplot as plt

allowedChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ,.?!"
targetGenome = "It was the best of times, it was the blurst of times"
mutateChance = .05
pop_size = 500
# percent of the best entities can breed
breed_num = .1
# percent of children they produce
child_num = .5
max_gens = 2000

class gen_entity:
    def __init__(self, genes=None):
        #generates genome either randomly or from parents
        if(genes == None):
            self.genome = ""
            for x in range(len(targetGenome)):
                self.genome += gen_entity.gen_mutated_gene()
        else:
            self.genome = genes
        self.fitness = self.calc_fitness()

    @classmethod
    def gen_mutated_gene(self):
        randChoice = random.random()
        #Either takes random char from set or mutates
        toReturn = ""
        if randChoice > mutateChance:
            return allowedChars[random.randint(0,len(allowedChars)-1)]
        #mutation can be add a character, remove a character, or random character
        randChoice = random.random()
        if randChoice <= (1/3) + .01:
            toReturn += allowedChars[random.randint(0,len(allowedChars)-1)]
            toReturn += allowedChars[random.randint(0,len(allowedChars)-1)]
        elif randChoice <= .68:
            toReturn += allowedChars[random.randint(0,len(allowedChars)-1)]
        return toReturn
        
    def calc_fitness(self):
        #every wrong character is -1, correct character is +1, incorrect length is -1
        fitness = 0
        for x in range(min(len(self.genome), len(targetGenome))):
            if self.genome[x] == targetGenome[x]:
                fitness += 1
            else:
                fitness -= 1
        if len(self.genome) < len(targetGenome):
            fitness -= (len(targetGenome) - len(self.genome))
        elif len(self.genome) > len(targetGenome):
            fitness -= (len(self.genome) - len(targetGenome))
            
        return fitness

    def make_child_genome(self, parent2):
        new_genome = ""
        for x in range(max(len(self.genome),len(parent2.genome))):
                randChoice = random.random()
                #Either takes attribute from either parent or mutates
                if randChoice < .5-mutateChance/2:
                    if x < len(self.genome):
                        new_genome += self.genome[x]
                elif randChoice > .5 + mutateChance/2:
                    if x < len(parent2.genome):
                        new_genome += parent2.genome[x]
                else:
                    #mutation can be add a character, remove a character, or random character
                    new_genome += gen_entity.gen_mutated_gene()
        return new_genome


entity_array = [gen_entity() for x in range(pop_size)]
entity_array.sort(key= lambda x: x.fitness, reverse=True)

historical_record = [entity_array[0]]
print("Initial Best Guess: " + entity_array[0].genome)
print("Initial Fitness: ", entity_array[0].fitness, "\n")

def breed_top_n(n, childNum):
    for x in range(int(childNum*pop_size)):
        parent1 = entity_array[random.randint(0,(n*pop_size)-1)]
        parent2 = entity_array[random.randint(0,(n*pop_size)-1)]
        entity_array[pop_size-1-x] = gen_entity(parent1.make_child_genome(parent2))

generationNum = 0
while(entity_array[0].genome != targetGenome and generationNum < max_gens):
    breed_top_n(breed_num, child_num)
    entity_array.sort(key= lambda x: x.fitness, reverse=True)
    historical_record.append(entity_array[0])
    generationNum += 1

print("Final Best Guess: " + entity_array[0].genome)
print("Final Fitness: ", entity_array[0].fitness, "\n")
print("After", generationNum, "Generations")

plotDecision = input("Plot results? (y/n)")
if(plotDecision.lower()[0] == 'y'):
    plt.plot([x.fitness for x in historical_record])
    plt.ylabel("fitness")
    plt.xlabel("generation")
    plt.title(targetGenome)
    plt.show()

printDecision = input("Print Log? (y/n)")
if(printDecision.lower()[0] == 'y'):
    for x in range(len(historical_record)):
        print("Generation:", x, historical_record[x].genome + " Fitness:",historical_record[x].fitness)

