from Delivery import *

d = Delivery.fromInputFile("example")


for w in d.warehouses:
    print(w)

for c in d.clients:
    print(c)

for p in d.products:
    print(p)
