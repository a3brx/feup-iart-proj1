from model.delivery import *
from algorithm.localsearch.hillclimbing import HillClimbing

if __name__ == "__main__":
    test = "example"

    model = Delivery.from_input_file(test)

    hillclimbing = HillClimbing(model)
    hillclimbing.run()

    # model.to_output_file(test)