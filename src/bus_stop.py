class BusStop:

    def __init__(self, name):
        self.name = name
        self.queue = []

    def queue_length(self):
        return len(self.queue)
    
    def add_to_queue(self, person):
        self.queue.append(person)
        # len(self.queue) #this line was not needed

    def clear(self):
        self.queue.clear()

    # def pick_up_from_stop(self):
    #     add_to_queue(person)
    #     bus.pick_up(person)
    #     self.clear()    



    # def sell_pet_to_customer(self, pet_name, customer):
    #     pet = self.find_pet_by_name(pet_name) 
    #     customer.reduce_cash(pet.price)
    #     self.increase_total_cash(pet.price)
    #     self.increase_pets_sold()
    #     self.remove_pet(pet)
    #     customer.add_pet(pet)    