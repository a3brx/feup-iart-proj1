from model.data import Data
from algorithm.localsearch.hillclimbing import HillClimbing
from algorithm.localsearch.simulatedannealing import SimulatedAnnealing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib


def plot_results(graphics):
    matplotlib.rc('figure', figsize=(50, 5))

    for label, solution_list in graphics.items():
        graphic = [[i for i, j in solution_list],
                [j.get_score() for i, j in solution_list]]
        plt.plot(graphic[0], graphic[1], label=label)

    plt.legend()
    plt.xticks(np.arange(0, graphic[0][-1], 250))
    plt.xlabel("iteration")
    plt.ylabel("score")

    plt.show()

def plot_hill_climbing(data, iterations=12750):
    search = HillClimbing(data, iterations)
    search.run()
    plot_results({
        "max score": search.solution_list
    })

def plot_simulated_annealing(data, iterations=12750):
    alphas = [80, 85, 90, 95, 99]

    annealings = [
        SimulatedAnnealing(data, iterations, 1000, alpha)
        for alpha in alphas
    ]
    for annealing in annealings:
        annealing.run()
    
    result = {}
    for index, alpha in enumerate(alphas):
        result["α = " + str(alpha) + "%"] = annealings[index].solution_list

    plot_results(result)

data = Data.from_input_file("busy_day")
plot_simulated_annealing(data, 20)
# solution.to_output_file(file)
