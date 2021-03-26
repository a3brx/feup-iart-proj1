from Delivery import *

if __name__ == "__main__":
    test = "busy_day"

    d = Delivery.fromInputFile(test)

    #for p in d.solution:
    #    print(p)

    print("Score:", d.evaluateSolution())

    d.toOutputFile(test)
