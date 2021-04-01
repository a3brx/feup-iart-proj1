from model.data import Data
from algorithm.localsearch.hillclimbing import HillClimbing
from algorithm.localsearch.simulatedannealing import SimulatedAnnealing

d = Data.from_input_file("busy_day")
SimulatedAnnealing(d).run()