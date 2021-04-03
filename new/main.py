from model.data import Data
from algorithm.localsearch.hillclimbing import HillClimbing
from algorithm.localsearch.simulatedannealing import SimulatedAnnealing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib


def plot_results(graphic):
    graphic = [[i for i, j in solution_list],
               [j.get_score() for i, j in solution_list]]

    matplotlib.rc('figure', figsize=(50, 5))

    plt.plot(graphic[0], graphic[1], 'ro')

    plt.show()


data = Data.from_input_file("busy_day")

search = HillClimbing(data, 50)
# search = SimulatedAnnealing(data, 1000, 1000, 0.9)
search.run()

solution_list = search.solution_list
plot_results(solution_list)
# solution.to_output_file(file)
