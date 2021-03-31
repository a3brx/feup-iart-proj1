from input.file_parsing import FileParsing
from algorithm.genetic.genetic import GeneticAlgorithm
from simulation.model.transportation import Transportation

if __name__ == "__main__":
    test = "example"

    simulation = FileParsing.parse("data/example.in")

    algorithm = GeneticAlgorithm(simulation, 5)
    algorithm.run()
