from Delivery import *

d = Delivery.fromInputFile("example")

d.warehouses[0].products[0].productType = 10

for p in d.products:
    print(p)