from model.delivery import *
from input.file_parsing import FileParsing
from algorithm.localsearch.hillclimbing import HillClimbing
from algorithm.localsearch.simulatedannealing import SimulatedAnnealing
from algorithm.genetic.genetic import GeneticAlgorithm

if __name__ == "__main__":
    test = "example"


    model = Delivery.from_input_file(test)
    simulatedannealing = SimulatedAnnealing(model)
    simulatedannealing.run()

    #simulation = FileParsing.parse("data/" + test + ".in")
    #algorithm = GeneticAlgorithm(simulation)
    #algorithm.random_solution()

    # model.to_output_file(test)
