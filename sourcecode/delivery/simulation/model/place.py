class Place:

    def __init__(self, location):
        self.location = location

    def __eq__(self, obj):
        return self.location == obj.location
