from delivery.algorithm.genetic.crossover import OrderCrossover
from delivery.input.file_parsing import FileParsing
from delivery.algorithm.genetic.genetic import GeneticAlgorithm
from delivery.algorithm.genetic.selection import RoulleteSelection, TournamentSelection
from delivery.simulation.model.transportation import Transportation
from delivery.output.output import save_solution


def run():
    test = "example"

    simulation = FileParsing.parse("data/fouroo.in")

    # selection = TournamentSelection(5)
    selection = RoulleteSelection()
    crossover = OrderCrossover()

    algorithm = GeneticAlgorithm(
        simulation, population_size=30, generational=False, crossover=crossover, selection_method=selection, mutation_probability=0.2, max_improveless_iterations=200)
    sol = algorithm.run().solution
    save_solution(sol, simulation)


if __name__ == "__main__":
    run()
