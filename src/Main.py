from Delivery import *

if __name__ == "__main__":
    test = "example"

    d = Delivery.fromInputFile(test)

    for p in d.solution:
        print(p)

    d.toOutputFile(test)