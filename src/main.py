from model.delivery import *
from input.file_parsing import FileParsing
from algorithm.localsearch.hillclimbing import HillClimbing
from algorithm.genetic.genetic import GeneticAlgorithm

if __name__ == "__main__":
    test = "example"

    simulation = FileParsing.parse("data/example.in")

    algorithm = GeneticAlgorithm(simulation)
    algorithm.random_solution()
    #model = Delivery.from_input_file(test)

    #hillclimbing = HillClimbing(model)
    # hillclimbing.run()

    # model.to_output_file(test)
