from model.data import Data
from algorithm.localsearch.hillclimbing import HillClimbing
from algorithm.localsearch.simulatedannealing import SimulatedAnnealing

file = "busy_day"
data = Data.from_input_file(file)

search = HillClimbing(data, 10)
# search = SimulatedAnnealing(data, 1000, 1000, 0.9)
search.run()

solution_list = search.solution_list
print(solution_list)
# solution.to_output_file(file)
