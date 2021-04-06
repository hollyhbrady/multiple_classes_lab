class BusStop:

    def __init__(self, bus_stop, queue):
        self.bus_stop = bus_stop

    def add_to_queue(self, person_1, person_2, bus_stop):
        


    def sell_pet_to_customer(self, pet_name, customer):
        pet = self.find_pet_by_name(pet_name) 
        customer.reduce_cash(pet.price)
        self.increase_total_cash(pet.price)
        self.increase_pets_sold()
        self.remove_pet(pet)
        customer.add_pet(pet)    