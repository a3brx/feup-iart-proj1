from model.delivery import *
from algorithm.localsearch.hillclimbing import HillClimbing
from algorithm.localsearch.simulatedannealing import SimulatedAnnealing

if __name__ == "__main__":
    test = "example"

    model = Delivery.from_input_file(test)

    simulatedannealing = SimulatedAnnealing(model)
    simulatedannealing.run()

    # model.to_output_file(test)