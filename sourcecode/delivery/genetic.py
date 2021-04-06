from delivery.output.command import Command
import delivery.input.file_parsing as file_parsing
from delivery.algorithm.genetic.crossover import OrderCrossover
from delivery.algorithm.genetic.genetic import GeneticAlgorithm
from delivery.algorithm.genetic.selection import RoulleteSelection, TournamentSelection
from delivery.output.output import save_solution


def read_from_file(filename):
    with open(filename, "r") as file:
        contents = file.read().splitlines()

    contents = contents[1:]

    drones = {}

    for line in contents:
        command = Command.from_string(line)

        if command.drone_id not in drones:
            drones[command.drone_id] = [command]
        else:
            drones[command.drone_id].append(command)

    return list(drones.values())


def run():
    simulation = file_parsing.parse("data/obvious.in")

    selection = TournamentSelection(15)
    #selection = RoulleteSelection()
    crossover = OrderCrossover()

    algorithm = GeneticAlgorithm(
        simulation, population_size=30, generational=True, crossover=crossover, selection_method=selection, mutation_probability=0.15, max_improveless_iterations=250, save_results=True)

    sol = algorithm.run().solution

    save_solution(sol, simulation)

    # print(algorithm.evaluate(sol))


if __name__ == "__main__":
    run()
