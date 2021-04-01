from algorithm.genetic.crossover import OrderCrossover
from input.file_parsing import FileParsing
from algorithm.genetic.genetic import GeneticAlgorithm
from algorithm.genetic.selection import TournamentSelection
from simulation.model.transportation import Transportation
from output.output import save_solution

if __name__ == "__main__":
    test = "example"

    simulation = FileParsing.parse("data/busy_day.in")

    selection = TournamentSelection(16)

    algorithm = GeneticAlgorithm(
        simulation, population_size=30, generational=True, selection_method=selection, iterations=100)
    sol = algorithm.run().solution
    save_solution(sol, simulation)
