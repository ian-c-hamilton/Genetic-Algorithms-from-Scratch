import datetime
import genetic
import random

geneset = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=,.,/<>[]:;'"
target = 'To be or not to be. That is the question!'


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)

def display(genes, target, startTime):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(genes, target)
    print("{}\t{}\t{}".format(genes, fitness, timeDiff))

def test_Hello_World():
    target = 'Hello World!'
    guess_password(target)

def guess_password(target):
    startTime = datetime.datetime.now()

    def fnGetFitness(genes):
        return get_fitness(genes, target)
    
    def fnDisplay(genes):
        display(genes, target, startTime)

    optimalFitness = len(target)
    best = genetic.get_best(fnGetFitness, len(target), optimalFitness, geneset, fnDisplay)

if __name__ == '__main__':
    test_Hello_World()