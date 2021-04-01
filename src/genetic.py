from algorithm.genetic.crossover import OrderCrossover
from input.file_parsing import FileParsing
from algorithm.genetic.genetic import GeneticAlgorithm
from algorithm.genetic.selection import TournamentSelection
from simulation.model.transportation import Transportation
from output.output import save_solution

if __name__ == "__main__":
    test = "example"

    simulation = FileParsing.parse("data/busy_day.in")

    selection = TournamentSelection(15)
    crossover = OrderCrossover()

    algorithm = GeneticAlgorithm(
        simulation, population_size=50, generational=False, crossover=crossover, mutation_probability=0.5, selection_method=selection, max_improveless_iterations=200)
    sol = algorithm.run().solution
    save_solution(sol, simulation)
