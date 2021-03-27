from math import sqrt, ceil
from collections import OrderedDict

from model.product import Product

class Place:
    calculated_distances = {}

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, operand):
        diff_x = abs(self.x - operand.x)
        diff_y = abs(self.y - operand.y)
        if diff_y < diff_x:
            tuple_key = (diff_y, diff_x)
        else:
            tuple_key = (diff_x, diff_y)
        if tuple_key in Place.calculated_distances.keys():
            return Place.calculated_distances[tuple_key]
        else:
            value = ceil(sqrt(diff_x * diff_x + diff_y * diff_y))
            Place.calculated_distances[tuple_key] = value
            return value

    def distance_to_product(self, product):
        return self.distance_to(product.last_place)

    def get_string_location(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Warehouse(Place):
    def __init__(self, warehouse_id, coordinates, items):
        super().__init__(*map(int, coordinates))
        self.id = warehouse_id
        self.create_products(map(int, items))

    def copy(self):
        copy_of_items = [
            product.product_type for product in self.products
        ]
        return Warehouse(self.id, (self.x, self.y), copy_of_items)

    def create_products(self, item_quantities):
        self.products = []
        for product_type, product_quantity in enumerate(item_quantities):
            products_of_type = [
                self.create_product(product_type)
                for _ in range(product_quantity)
            ]
            self.products.extend(products_of_type)

    def create_product(self, product_type):
        return Product(int(product_type), self)

    def __str__(self):
        return "Warehouse at " + self.get_string_location()


class Client(Place):
    def __init__(self, client_id, coordinates, products):
        super().__init__(*map(int, coordinates))
        self.id = client_id
        self.wanted_products = list(map(int, products))

    def __str__(self):
        return "Client at " + self.get_string_location()

    def __len__(self):
        return len(self.wanted_products)
