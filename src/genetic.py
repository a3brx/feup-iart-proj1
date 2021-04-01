from algorithm.genetic.crossover import OrderCrossover
from input.file_parsing import FileParsing
from algorithm.genetic.genetic import GeneticAlgorithm
from algorithm.genetic.selection import RoulleteSelection, TournamentSelection
from simulation.model.transportation import Transportation
from output.output import save_solution

if __name__ == "__main__":
    test = "example"

    simulation = FileParsing.parse("data/busy_day.in")

    selection = TournamentSelection(5)
    # selection = RoulleteSelection()
    crossover = OrderCrossover()

    algorithm = GeneticAlgorithm(
        simulation, population_size=30, generational=True, crossover=crossover, selection_method=selection, mutation_probability=0.2, max_improveless_iterations=200)
    sol = algorithm.run().solution
    print(sol)
    save_solution(sol, simulation)
