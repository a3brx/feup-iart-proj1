from delivery.model.data import Data
from delivery.algorithm.localsearch.hillclimbing import HillClimbing
from delivery.algorithm.localsearch.simulatedannealing import SimulatedAnnealing

def run():
    data = Data.from_input_file("data/custom.in")

    algorithm = HillClimbing(data, 1000)

    sol = algorithm.run()

    # print(algorithm.evaluate(sol))


if __name__ == "__main__":
    run()
