from Delivery import *

d = Delivery.fromInputFile("example")

for p in d.products:
    print(p)
