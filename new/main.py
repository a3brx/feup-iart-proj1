from model.data import Data
from algorithm.localsearch.hillclimbing import HillClimbing
from algorithm.localsearch.simulatedannealing import SimulatedAnnealing

file = "obvious"

d = Data.from_input_file(file)
solution = SimulatedAnnealing(d).run()
solution.to_output_file(file)
