import delivery.input.file_parsing as file_parsing
from delivery.algorithm.localsearch.hillclimbing import HillClimbing
from delivery.output.output import save_solution


def run():
    simulation = file_parsing.parse("data/busy_day.in")

    algorithm = HillClimbing(simulation)

    sol = algorithm.run()

    save_solution(sol, simulation)

    # print(algorithm.evaluate(sol))


if __name__ == "__main__":
    run()
