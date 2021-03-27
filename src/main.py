from model.delivery import *
from algorithm.localsearch.hillclimbing import HillClimbing

if __name__ == "__main__":
    test = "example"

    model = Delivery.from_input_file(test)

    for path in model.solution:
        print(path)

    print("Score:", model.evaluate_solution())

    hillclimbing = HillClimbing(model)
    hillclimbing.run()

    for path in model.solution:
        print(path)

    print("Score:", model.evaluate_solution())

    # model.to_output_file(test)