# Delivery With Drones

## Execution and Results

### Notebook

To get a full study on the problem, one can check the `delivery.ipynb` notebook.

### Manual Configuration

Tu run the program with a desired configuration, it receives a JSON input file (for example `python main.py genetic.json`).

#### Required JSON Values

- **input**: the input file, required
- **output**: the output file, required

##### Genetic

```json
{
    "input_file": "data/fouroo.in",
    "output_file": "test1.out",
    "algorithm": {
        "name": "genetic",
        "time": "20",
        "iterations": "2",
        "max_improveless_iterations": "30",
        "selection_method": "tournament",
        "tournament_size": "10",
        "crossover": "order",
        "population_size" : "30",
        "generational": "True",
        "mutation_probability": "0.2",
        "log": "True",
        "save_results": "False"
    }
}
```

- **algorithm**: required
    - **name**: the algorithm, required, should be genetic
    - **time**: the max time the algorithm can take in seconds
    - **iterations**: the max possible number of iterations
    - **max_improveless_iterations**: the max number of improveless iterations, default 20
    - **selection_method**: the selection method, default is tournament, should be in {tournament, roullete}
    - **tournament_size**: the size of the tournament (only in tournament selections)
    - **crossover**: the crossover, default ir order, should be in {order, one_point}
    - **population_size** : the size of the population, default is 30
    - **generational**: if the algorithm runs through generations or iterations
    - **mutation_probability**: the probability of mutations, default is 0.2
    - **log**: if displays results in real time, default is true
    - **save_results**: if saves the results to a file, default is false

##### Hill Climbing

```json
{
    "input_file": "data/fouroo.in",
    "output_file": "test2.out",
    "algorithm": {
        "name": "hill_climbing",
        "max_iterations": "2"
    }
}
```

- **algorithm**: required
    - **max_iterations**: the max possible number of iterations
    - **iteration_search**: the number of neighbours generated per iteration

##### Simulated Annealing

```json
{
    "input_file": "data/fouroo.in",
    "output_file": "test3.out",
    "algorithm": {
        "name": "simulated_annealing",
        "max_iterations": "2",
        "temperature_schedule": "0.9",
        "initial_temperature": "1000"
    }
}
```

- **algorithm**: required
    - **max_iterations**: the max possible number of iterations
    - **iteration_search**: the number of neighbours generated per iteration
    - **temperature_schedule**: the time schedule, the factor that will define the rate of decreasing in temperature
    - **initial_temperature**: the initial temperature

The `genetic.json` and `hill_climbing.json` are given in this repo.