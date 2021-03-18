class Path:
    #drone

    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def time(self):
        return self.origin.distance(self.destination)