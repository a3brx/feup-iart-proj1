from model.place import Position


class Drone:
    def __init__(self, drone_id):
        self.id = drone_id

    def __str__(self):
        return "d" + str(self.id)

    def copy(self):
        return self