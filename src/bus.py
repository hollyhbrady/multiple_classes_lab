class Bus:

    import pdb

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

    def pick_up_from_stop(self, person):
        # pdb.stacktrace()
        bus_stop.add_to_queue(person)
        self.pick_up(person)
        bus_stop.clear() 


        # def sell_pet_to_customer(self, pet_name, customer):
        # pet = self.find_pet_by_name(pet_name) 
        # customer.reduce_cash(pet.price)
        # self.increase_total_cash(pet.price)
        # self.increase_pets_sold()
        # self.remove_pet(pet)
        # customer.add_pet(pet)

