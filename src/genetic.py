from algorithm.genetic.crossover import OrderCrossover
from input.file_parsing import FileParsing
from algorithm.genetic.genetic import GeneticAlgorithm
from algorithm.genetic.selection import TournamentSelection
from simulation.model.transportation import Transportation

if __name__ == "__main__":
    test = "example"

    simulation = FileParsing.parse("data/busy_day.in")

    algorithm = GeneticAlgorithm(
        simulation, population_size=4, generational=True)
    print(algorithm.run().solution)
