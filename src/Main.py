from Delivery import *

if __name__ == "__main__":
    d = Delivery.fromInputFile("example")

    for p in d.solution:
        print(p)
