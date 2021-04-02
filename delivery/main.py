from model.delivery import *
import delivery.input.file_parsing as file_parsing
from delivery.algorithm.localsearch.hillclimbing import HillClimbing
from delivery.algorithm.genetic.genetic import GeneticAlgorithm

if __name__ == "__main__":
    test = "example"

    simulation = file_parsing.parse("data/example.in")

    algorithm = GeneticAlgorithm(simulation)
    algorithm.random_solution()
    #model = Delivery.from_input_file(test)

    #hillclimbing = HillClimbing(model)
    # hillclimbing.run()

    # model.to_output_file(test)
