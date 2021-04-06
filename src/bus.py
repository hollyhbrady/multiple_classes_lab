class Bus:

    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        # self.queue_length = queue_length
        # self.stop_name = stop_name
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        return self.passengers.append(person)

    def drop_off(self, person):
        return self.passengers.remove(person)

    def empty(self):
        return self.passengers.clear()

