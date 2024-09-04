from lion import Lion
from tiger import Tiger
from cheetah import Cheetah
from keeper import Keeper
from caretaker import Caretaker
from vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal:isinstance, price):
        if len(self.animals) < self.__animal_capacity:
            if price <= self.__budget:
                self.animals.append(animal)
                self.__budget -= price
                return self.__budget and f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            else:
                return "Not enough budget"
        else:
            return "Not enough space for animal"
        
    def hire_worker(self, worker:isinstance):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"
        
    def fire_worker(self, worker_name:str):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"    
    
    def pay_workers(self):
        sum_salary = sum(worker.salary for worker in self.workers)
        if sum_salary <= self.__budget:
            self.__budget -= sum_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"
    
    def tend_animals(self):
        sum_tend = sum(animal.get_needs() for animal in self.animals)
        if sum_tend <= self.__budget:
            self.__budget -= sum_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."
    
    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        amount_of_lions = [animal for animal in self.animals if type(animal)==Lion]
        amount_of_tigers = [animal for animal in self.animals if type(animal)==Tiger]
        amount_of_cheetahs = [animal for animal in self.animals if type(animal)==Cheetah]

        status = []
        status.append("You have {} animals".format(len(self.animals)))

        status.append("----- {} Lions:".format(len(amount_of_lions)))
        for lion in amount_of_lions:
            status.append("{}".format(lion.__repr__()))

        status.append("----- {} Tigers:".format(len(amount_of_tigers)))
        for tiger in amount_of_tigers:
            status.append("{}".format(tiger.__repr__()))

        status.append("----- {} Cheetahs:".format(len(amount_of_cheetahs)))
        for cheetah in amount_of_cheetahs:
            status.append("{}".format(cheetah.__repr__()))
            
        return "\n".join(status)
    
    def workers_status(self):
        amount_of_keepers = [worker for worker in self.workers if type(worker)==Keeper]
        amount_of_caretakers = [worker for worker in self.workers if type(worker)==Caretaker]
        amount_of_vetes = [worker for worker in self.workers if type(worker)==Vet]

        status = []
        status.append("You have {} workers".format(len(self.workers)))

        status.append("----- {} Keepers:".format(len(amount_of_keepers)))
        for keeper in amount_of_keepers:
            status.append("{}".format(keeper.__repr__()))

        status.append("----- {} Caretakers:".format(len(amount_of_caretakers)))
        for caretaker in amount_of_caretakers:
            status.append("{}".format(caretaker.__repr__()))

        status.append("----- {} Vetes:".format(len(amount_of_vetes)))
        for vet in amount_of_vetes:
            status.append("{}".format(vet.__repr__()))
            
        return "\n".join(status)       
        