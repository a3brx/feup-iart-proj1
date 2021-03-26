from model.delivery import *

if __name__ == "__main__":
    test = "busy_day"

    d = Delivery.from_input_file(test)

    #for p in d.solution:
    #    print(p)

    print("Score:", d.evaluate_solution())

    d.to_output_file(test)