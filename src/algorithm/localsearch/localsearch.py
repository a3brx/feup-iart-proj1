from algorithm.mutation import *

class LocalSearch:
    def __init__(self, model):
        self.model = model
    
    def swap_operations(self):
        swap_operations(self.model)

    def insert_operation(self):
        insert_operation(self.model)

    def remove_operation(self):
        remove_operation(self.model)

    def switch_operation_drone(self):
        switch_operation_drone(self.model)

