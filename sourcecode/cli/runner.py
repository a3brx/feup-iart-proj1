from delivery.algorithm.genetic.crossover import OnePointCrossover, OrderCrossover
from delivery.algorithm.genetic.selection import RoulleteSelection, TournamentSelection
import inspect

import delivery.input.file_parsing as file_parsing
from delivery.model.data import Data
from delivery.algorithm.genetic.genetic import GeneticAlgorithm
from delivery.algorithm.localsearch.hillclimbing import HillClimbing
from delivery.algorithm.localsearch.simulatedannealing import SimulatedAnnealing
from delivery.output.output import save_solution

from cli.json_parser import JsonObject, JsonParser, JsonValue


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


class Runner:

    available_algorithms = {'genetic': GeneticAlgorithm,
                            'hill_climbing': HillClimbing,
                            "simulated_annealing": SimulatedAnnealing}

    def __init__(self, input_file, output_file, algorithm, arguments):
        self.input_file = input_file
        self.output_file = output_file
        self.algorithm = algorithm
        self.arguments = arguments

    @classmethod
    def build(cls, json):
        input_file = json.get("input_file")
        output_file = json.get("output_file")

        algorithm = json.get_object("algorithm")
        algorithm_json = JsonParser(algorithm)

        algorithm_name = algorithm_json.get(
            "name", Runner.available_algorithms.keys())

        AlgorithmClass = Runner.available_algorithms[algorithm_name]

        arguments = Runner.__algorithm_args(algorithm_name, algorithm_json)

        return cls(input_file, output_file, AlgorithmClass, arguments)

    def run(self):
        simulation = file_parsing.parse(self.input_file) if self.algorithm == GeneticAlgorithm else Data.from_input_file(self.input_file)
        tournament_size = -1
        if "tournament_size" in self.arguments:
            tournament_size = self.arguments["tournament_size"]
            del self.arguments["tournament_size"]

        algorithm_obj = self.algorithm(simulation, **self.arguments)

        if "selection_method" in self.arguments:
            method = self.arguments["selection_method"]

            if method == "tournament":
                if tournament_size < 0:
                    tournament_size = 10

                tournament = TournamentSelection(tournament_size)

                algorithm_obj.selection_method = tournament

            elif method == "roullete":
                roullete = RoulleteSelection()

                algorithm_obj.selection_method = roullete

        if "crossover" in self.arguments:
            crossover = self.arguments["crossover"]

            if crossover == "one_point":
                algorithm_obj.crossover = OnePointCrossover()

            elif crossover == "order":
                algorithm_obj.crossover = OrderCrossover()
    
        # runs the algorithm
        res = algorithm_obj.run()
        if hasattr(res, 'solution'):
            res = res.solution

        if self.algorithm == GeneticAlgorithm:
            save_solution(res, simulation, self.output_file)
        else:
            res.to_output_file(self.output_file)

    def __algorithm_args(algorithm_name, json):
        if algorithm_name == 'genetic':
            return Runner.__genetic_args(json)
        elif algorithm_name == 'hill_climbing':
            return Runner.__hill_args(json)
        elif algorithm_name == 'simulated_annealing':
            return Runner.__simulated_annealing(json)

    def __genetic_args(json):
        args = {}

        time = json.get('time', required=False)
        if time is not None:
            args['time'] = int(time)

        iterations = (json.get('iterations', required=False))
        if iterations is not None:
            args['iterations'] = int(iterations)

        max_improveless_iterations = (
            json.get('max_improveless_iterations', required=False))

        if max_improveless_iterations is not None:
            args['max_improveless_iterations'] = int(
                max_improveless_iterations)

        population_size = (json.get('population_size', required=False))
        if population_size is not None:
            args['population_size'] = int(population_size)

        generational = (json.get('generational', required=False))
        if generational is not None:
            args['generational'] = str2bool(generational)

        mutation_probability = (
            json.get('mutation_probability', required=False))
        if mutation_probability is not None:
            args['mutation_probability'] = float(mutation_probability)

        log = (json.get('log', required=False))
        if log is not None:
            args['log'] = str2bool(log)

        save_results = (json.get('save_results', required=False))
        if save_results is not None:
            args['save_results'] = str2bool(save_results)

        crossover = (json.get('crossover', required=False))
        if crossover is not None:
            args['crossover'] = (crossover)

        selection_method = (json.get('selection_method', required=False))
        if selection_method is not None:
            args['selection_method'] = (selection_method)

        tournament_size = (json.get('tournament_size', required=False))
        if tournament_size is not None:
            args['tournament_size'] = int(tournament_size)

        return args

    def __hill_args(json):
        args = {}

        max_iterations = (json.get('max_iterations', required=False))
        if max_iterations is not None:
            args['max_iterations'] = int(max_iterations)

        iteration_search = (json.get('iteration_search', required=False))
        if iteration_search is not None:
            args['iteration_search'] = int(iteration_search)

        save_results = (json.get('save_results', required=False))
        if save_results is not None:
            args['save_results'] = str2bool(save_results)

        return args

    def __simulated_annealing(json):
        args = {}

        max_iterations = (json.get('max_iterations', required=False))
        if max_iterations is not None:
            args['max_iterations'] = int(max_iterations)

        iteration_search = (json.get('iteration_search', required=False))
        if iteration_search is not None:
            args['iteration_search'] = int(iteration_search)

        temperature_schedule = (json.get('temperature_schedule', required=False))
        if temperature_schedule is not None:
            args['temperature_schedule'] = float(temperature_schedule)

        initial_temperature = (json.get('initial_temperature', required=False))
        if initial_temperature is not None:
            args['initial_temperature'] = int(initial_temperature)

        save_results = (json.get('save_results', required=False))
        if save_results is not None:
            args['save_results'] = str2bool(save_results)

        return args